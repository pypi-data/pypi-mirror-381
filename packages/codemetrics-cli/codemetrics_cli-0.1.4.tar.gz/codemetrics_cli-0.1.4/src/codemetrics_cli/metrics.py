import sys
import os
import hashlib
import subprocess
import xml.etree.ElementTree as ET
from tabulate import tabulate
from colorist import Color
import argparse
import math
from datetime import datetime, timedelta
from uniplot import plot
from pathlib import Path
import numpy as np

current_path = os.getcwd()
roslyn_github_repo = "https://github.com/dotnet/roslyn.git"
homedir = os.path.expanduser("~")
internal_stuff_path = os.path.join(homedir, ".metrics_scratch")
cloned_repos = os.path.join(internal_stuff_path, "repos")
metrics_exe = os.path.join(internal_stuff_path, "roslyn", "artifacts", "bin", "Metrics", "Release", "net472", "Metrics.exe")
remote_url = ""
main_repo_path = ""
shadow_repo_path = ""
working_repo_path = ""
verbose = False

GITIGNORED_FILES_THAT_AFFECT_THE_BUILD = []

def figure_out_paths_get_target(args, use_shadow_repo):
    global shadow_repo_path, remote_url, verbose, main_repo_path

    verbose = args.verbose
    
    if args.solution is not None:
        anchor = args.solution
    else:
        anchor = args.project
    
    anchor = Path(anchor).absolute()
    chdir(anchor.parent)
    
    # okay. so. we need a proper path for a target file to pass along to metrics.exe
    # user is providing either an absolute or a relative version of this path
    # however, we may need to run it against a shadow repo
    # so need to sub
    
    main_repo_path = Path(run_cmd_checked(["git", "rev-parse", "--show-toplevel"], capture_output=True).stdout.decode("utf-8").replace("\n", "")).absolute().__str__()
    remote_url = run_cmd_checked(["git", "remote", "get-url", args.origin], capture_output=True).stdout.decode("utf-8").replace("\n", "")
    repo_name = remote_url.split("/")[-1]
    shadow_repo_path = Path(os.path.join(cloned_repos, repo_name)).absolute().__str__()
    chdir(current_path)
    
    if args.solution is not None:
        is_solution = True
        args.solution = Path(args.solution).absolute().resolve().__str__()
        if use_shadow_repo:
            target_path = args.solution.replace(main_repo_path, shadow_repo_path)
        else:
            target_path = args.solution

        target = (is_solution, target_path)
    elif args.project is not None:
        is_solution = False
        args.project = Path(args.project).absolute().resolve().__str__()
        if use_shadow_repo:
            target_path = args.project.replace(main_repo_path, shadow_repo_path)
        else:
            target_path = args.project

        target = (is_solution, target_path)
    
    return target

def internal_setup(force_update, force_update_hard, branch):
    install_metrics_tool()

    if not os.path.isdir(cloned_repos):
        os.mkdir(cloned_repos)
    
    update_shadow_repo(force_update, force_update_hard, branch)

def cli():
    parser = argparse.ArgumentParser(description="CodeMetrics CLI helper for dotnet projects")
    parser.add_argument('-p', '--project', help="Project to analyze")
    parser.add_argument('-s', '--solution', help="Solution to analyze")
    parser.add_argument('-n', '--namespace', help="Show metrics for all types within a namespace (when analyzing a project)")
    parser.add_argument('-c', '--commit', help="git commit hash to use for metrics")
    parser.add_argument('-dc', '--diff_commits', help="fromHash..untilHash, compare metrics at these two states of the repo")
    parser.add_argument('-dd', '--diff_dates', help="fromDate..untilDate, compare metrics at these two points in time, e.g. 2024-01-30..2025-01-30")
    parser.add_argument('-st', '--step', help="When running diff_dates or diff_commits, take measurements at a specified day or commit interval")
    parser.add_argument('-pl', '--plot', help="Plot results of diffing over time. Specify which metric to plot")
    parser.add_argument('-a', '--absolute', action="store_true", help="Show absolute values instead of percentages when diffing")
    parser.add_argument('-o', '--origin', default="origin", help="Name of upstream git remote")
    parser.add_argument('-f', '--force_update', action='store_true', help="Update shadow repo by pulling remote and recalculate metrics regarding of cache state")
    parser.add_argument('-ff', '--force_update_hard', action='store_true', help="Update shadow repo by deleting local branch and pulling remote and recalculate metrics regarding of cache state")
    parser.add_argument('-b', '--branch', default="master", help="Name of the branch on which to run analysis; defaults to 'master'")
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help="Print out in detail of what's going on")
    args = parser.parse_args()

    recalculate_metrics = args.force_update or args.force_update_hard
    
    # TODO:
    # - absolute or % change for table diff
    # - add usage samples
    # - plot by commits
    
    if args.solution is None and args.project is None:
        parser.print_usage()
        exit(1)
    
    use_shadow_repo = False
    if args.diff_dates is not None or args.diff_commits is not None or args.commit is not None:
        use_shadow_repo = True
    
    target = figure_out_paths_get_target(args, use_shadow_repo)
    is_solution = target[0]
    internal_setup(args.force_update, args.force_update_hard, args.branch)

    if (args.diff_commits is not None or args.commit is not None) and not check_presence_of_commits(use_shadow_repo, args.diff_commits, args.commit):
        print("Invalid commits supplied, check your inputs or try rerunning with -f or -ff")
        exit(1)

    if args.commit is not None:
        metrics_xml = gather_metrics(target, recalculate_metrics, args.commit)
        headers, rows = process_metrics(metrics_xml, is_solution, args.namespace)
        print_metrics(headers, rows)

    elif args.diff_dates is not None and args.step is None:
        dates = args.diff_dates.split("..")
        date_from, date_until = dates[0], dates[1]
        hash_before = run_cmd(["git", "log", f"--until={date_from}", "-n", "1", "--format=oneline"], capture_output=True).stdout.decode("utf-8").split(" ")[0]
        hash_after = run_cmd(["git", "log", f"--until={date_until}", "-n", "1", "--format=oneline"], capture_output=True).stdout.decode("utf-8").split(" ")[0]
        print(f"{Color.GREEN}Diff between {date_from} and {date_until}{Color.OFF}")
        print(f"{Color.GREEN}Dates resolved to commit range {hash_before}..{hash_after}{Color.OFF}")
        do_diff(args.absolute, target, recalculate_metrics, args.namespace, is_solution, hash_before, hash_after)
    
    elif args.diff_dates is not None and args.step is not None:
        dates = args.diff_dates.split("..")
        date_from = datetime.strptime(dates[0], "%Y-%m-%d")
        date_until = datetime.strptime(dates[1], "%Y-%m-%d")
        step = args.step
        
        print(f"{Color.GREEN}Diff between {date_from.date()} and {date_until.date()}, checking every {step} day(s), on branch {args.branch}{Color.OFF}")
        
        calc_date = date_until
        check_dates_hashes = []
        stepped_over_date_from = False
        while calc_date >= date_from and not stepped_over_date_from:
            check_date = calc_date.strftime("%Y-%m-%d")
            check_hash = run_cmd(["git", "log", f"--until={check_date}", "-n", "1", "--format=oneline"], capture_output=True).stdout.decode("utf-8").split(" ")[0]
            if check_hash == "":
                print(f"Couldn't find a commit hash for a given date {check_date}; try adjusting your time range or force-updating via -f or -ff")
                exit(1)

            check_dates_hashes.append((check_date, check_hash))
            calc_date = calc_date - timedelta(days=int(step))
            # Make sure to include date_from in the calculations.
            if calc_date < date_from:
                stepped_over_date_from = True
                calc_date = date_from
        
        compute_metrics_for_commits_and_plot("Date", check_dates_hashes, target, recalculate_metrics, is_solution, args.namespace, args.plot)
    
    elif args.diff_commits is not None and args.step is None:
        hashes = args.diff_commits.split("..")
        hash_before, hash_after = hashes[0], hashes[1]
        print(f"{Color.GREEN}Diff between {hash_before} and {hash_after}{Color.OFF}")
        do_diff(args.absolute, target, recalculate_metrics, args.namespace, is_solution, hash_before, hash_after)
    
    elif args.diff_commits is not None and args.step is not None:
        hashes = args.diff_commits.split("..")
        hash_before, hash_after = hashes[0], hashes[1]
        print(f"{Color.GREEN}Diff between {hash_before} and {hash_after}, checking every {args.step} commit(s){Color.OFF}")
        
        commits = []
        # %h is to get abbrev-commit instead of full 40 byte commit hash, it looks nicer in the terminal.
        # When inserting hash_before, truncate it in the same way assuming constant commit object name (aka commit hash) prefix length.
        out = run_cmd(["git", "log", f"{hash_before}..{hash_after}", "--pretty=%h"], capture_output=True).stdout.decode("utf-8")
        commits = out.split("\n")
        commits[-1] = hash_before[:(len(commits[0]))] # last element from above split is empty line, and output excludes hash_before
        commits.reverse()
        labeled_commits = [(f"{i+1}: {c}", c) for (i, c) in enumerate(commits)]
        labeled_commits = labeled_commits[::int(args.step)]
        compute_metrics_for_commits_and_plot("Commit", labeled_commits, target, recalculate_metrics, is_solution, args.namespace, args.plot)

    else:
        metrics_xml = gather_metrics(target, recalculate_metrics, None)
        headers, rows = process_metrics(metrics_xml, is_solution, args.namespace)
        print_metrics(headers, rows)

def compute_metrics_for_commits_and_plot(label_title, labeled_commits, target, recalculate_metrics, is_solution, namespace, should_plot):
    if label_title == "Date":
        print(f"{Color.GREEN}Resolved to following range: {labeled_commits}{Color.OFF}")
    elif label_title == "Commit":
        print(f"{Color.GREEN}Resolved to following range: {[c[1] for c in labeled_commits]}{Color.OFF}")

    plot_rows = []

    for i, (label, commit) in enumerate(labeled_commits):
        print(f"{Color.GREEN}Processing {i + 1} / {len(labeled_commits)}{Color.OFF}")
        check_xml = gather_metrics(target, recalculate_metrics, commit)
        headers, rows = process_metrics(check_xml, is_solution, namespace)
        total_row = rows[-1:]
        total_row[0][0] = label
        plot_rows.extend(total_row)
        
    headers[0] = f"{Color.MAGENTA}{label_title}{Color.OFF}"
    print_metrics(headers, plot_rows)
    
    if should_plot is not None:
        a = np.array(plot_rows)
        t = np.transpose(a)
        
        if should_plot == "all":
            metrics = ["MaintainabilityIndex", "CyclomaticComplexity", "ClassCoupling", "DepthOfInheritance", "SourceLines", "ExecutableLines"]
        else:
            metrics = should_plot.split(",")

        for metric in metrics:
            if metric == "MaintainabilityIndex":
                di = 1
            elif metric == "CyclomaticComplexity":
                di = 2
            elif metric == "ClassCoupling":
                di = 3
            elif metric == "DepthOfInheritance":
                di = 4
            elif metric == "SourceLines":
                di = 5
            elif metric == "ExecutableLines":
                di = 6
            
            print()

            if label_title == "Date":
                plot(xs=[t[0]], ys=[t[di]], lines=True, title=metric)
            elif label_title == "Commit":
                plot(xs=None, ys=[t[di]], lines=True, title=metric)

            print()

def check_presence_of_commits(use_shadow_repo, diff_commits, commit):
    repo = main_repo_path
    if use_shadow_repo:
        repo = shadow_repo_path

    to_check = []
    if diff_commits is not None:
        hashes = diff_commits.split("..")
        to_check.append(hashes[0])
        to_check.append(hashes[1])
    elif commit is not None:
        to_check.append(commit)
    
    for hash in to_check:
        chdir(repo)
        out = run_cmd(["git", "cat-file", "-t", hash], capture_output=True).stdout.decode("utf-8").replace("\n", "")
        if out != "commit":
            print("Commit with hash {} does not exist", hash)
            return False
    return True

def do_diff(show_abs, target, recalculate_metrics, namespace, is_solution, hash_before, hash_after):
    before_xml = gather_metrics(target, recalculate_metrics, hash_before)
    headers_0, rows_0 = process_metrics(before_xml, is_solution, namespace)

    after_xml = gather_metrics(target, recalculate_metrics, hash_after)
    headers_1, rows_1 = process_metrics(after_xml, is_solution, namespace)
    
    headers, rows = diff_metrics(show_abs, headers_0, rows_0, headers_1, rows_1)
    print_metrics(headers, rows)
    
def gather_metrics(target, force_update, commit_hash):
    is_solution, target_path = target
    if is_solution:
        metrics_cmd = "s"
    else:
        metrics_cmd = "p"

    if commit_hash is not None:
        chdir(shadow_repo_path)

        # Take into account both target and commit.
        contents_hash = hashlib.sha256()
        contents_hash.update(str.encode(f"{metrics_cmd}{target_path}"))
        contents_hash.update(str.encode(commit_hash[:8])) # abbrev-commit
        repo_hash = contents_hash.hexdigest()
    else:
        chdir(main_repo_path)
        repo_hash = current_repo_hash(target)

    metrics_out = os.path.join(internal_stuff_path, f"{repo_hash}.xml")
    if force_update or not os.path.isfile(metrics_out):
        if commit_hash is not None:
            run_cmd(["git", "checkout", commit_hash])
        run_cmd([metrics_exe, f"/{metrics_cmd}:{target_path}", f"/o:{metrics_out}"], check=True)
    
    return metrics_out

def process_metrics(metrics_xml, is_solution, namespace_filter):
    tree = ET.parse(metrics_xml)
    root = tree.getroot()

    # ugh this is horrible and solution part doesn't work
    if not is_solution:
        target_root = root[0][0][0][1]
        if namespace_filter is None:
            headers, rows = parse_metrics_from_root(target_root)
        else:
            for ns in target_root:
                if ns.get('Name') != namespace_filter:
                    continue
                headers, rows = parse_metrics_from_root(ns.find('Types'))
        
        total_row = get_total_row(rows)
        rows.append(total_row)
        return headers, rows

    else:
        headers = []
        all_rows = []

        for project in root[0]:
            target_root = project
            if namespace_filter is None:
                headers, rows = parse_metrics_from_root(target_root)
            else:
                for ns in target_root:
                    if ns.get('Name') != namespace_filter:
                        continue
                    headers, rows = parse_metrics_from_root(ns.find('Types'))
            all_rows.extend(rows)

        total_row = get_total_row(all_rows)
        all_rows.append(total_row)
        return headers, all_rows


def diff_metrics(show_abs, headers_0, rows_0, headers_1, rows_1):
    if headers_0 != headers_1:
        raise SystemExit("Metric dimensions do not match")
    metric_count = len(headers_0) - 1 # -1 to account for 'Namespace' being part of headers, while it's not a metric
    
    delta = []
    metrics_0 = {}
    metrics_1 = {}
    for row in rows_0:
        metrics_0[row[0]] = row[1:]

    for row in rows_1:
        metrics_1[row[0]] = row[1:]
    
    for m in metrics_1.keys():
        delta_row = [m]
        if m in metrics_0:
            for i in range(metric_count):
                if float(metrics_0[m][i]) == 0:
                    delta_row.append("∞")
                else:
                    # absolute diff or % diff
                    value_symbol = ""
                    if show_abs:
                        rounded = int(metrics_1[m][i] - metrics_0[m][i])
                    else:
                        perc_delta = 100 * (float(metrics_1[m][i]) - float(metrics_0[m][i])) / float(metrics_0[m][i])
                        rounded = math.ceil(perc_delta * 100) / 100
                        value_symbol = "%"

                    set_color = True
                    if m == "MaintainabilityIndex":
                        if rounded > 0:
                            color = Color.GREEN
                        elif rounded < 0:
                            color = Color.RED
                        else:
                            set_color = False
                    else:
                        if rounded > 0:
                            color = Color.RED
                        elif rounded < 0:
                            color = Color.GREEN
                        else:
                            set_color = False
                    if set_color:
                        delta_row.append(f"{color}{rounded}{value_symbol}{Color.OFF}")
                    else:
                        delta_row.append(f"{rounded}{value_symbol}")
        else:
            # m only present in the "_1" aka "after".
            # can't diff, so display either raw value or infinity symbol
            for i in range(metric_count):   
                if show_abs:
                    delta_row.append(f"new: {int(metrics_1[m][i])}")
                else:
                    delta_row.append("∞")
        delta.append(delta_row)
    
    # last row is the 'Total', separate it out for now
    total_row = delta[-1]
    delta.remove(delta[-1])
    
    # show what is no longer present in _1:
    for m in metrics_0.keys():
        if m in metrics_1:
            continue
        
        delta_row = [m]
        for i in range(metric_count):
            if show_abs:
                delta_row.append(f"{Color.GREEN}-{int(metrics_0[m][i])}{Color.OFF}")
            else:
                delta_row.append(f"{Color.GREEN}-100%{Color.OFF}")
        delta.append(delta_row)
    
    print(delta[-9])

    # add 'Total' row back in
    delta.append(total_row)
    return headers_0, delta

def print_metrics(headers, rows):
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

def parse_metrics_from_root(metrics_root):
    rows = []
    headers = [f"{Color.MAGENTA}Namespace{Color.OFF}"]
    for obj in metrics_root:
        row = []
        row.append(f"{Color.CYAN}{obj.get('Name')}{Color.OFF}")
        for child in obj.find('Metrics'):
            colored_header = f"{Color.MAGENTA}{child.get('Name')}{Color.OFF}"
            if colored_header not in headers:
                headers.append(colored_header)
            row.append(float(child.get('Value')))
        rows.append(row)
    
    return (headers, rows)

def get_total_row(rows):
    total_row = [f"{Color.MAGENTA}Total{Color.OFF}"]
    for row in rows:
        for i, v in enumerate(row[1:]):
            try:
                total_row[i+1] = total_row[i+1] + v
            except IndexError:
                total_row.append(v)
    
    # first column is maintainability index, we take an average of that instead of a sum
    # to match what CodeAnalysis.Metrics package does when aggregating.
    total_row[1] = math.ceil((total_row[1]) / len(rows) * 100) / 100
                
    return total_row

def update_shadow_repo(update, update_hard, branch):
    if os.path.isdir(shadow_repo_path):
        if update:
            print("Updating shadow repo branch...")
            chdir(shadow_repo_path)
            run_cmd(["git", "fetch", "--all"])
            run_cmd(["git", "checkout", branch])
            run_cmd(["git", "pull"])
        elif update_hard:
            print("Hard resetting shadow repo branch...")
            chdir(shadow_repo_path)
            run_cmd(["git", "fetch", "--all"])
            run_cmd(["git", "reset", "--hard", branch])
        chdir(main_repo_path)
    else:
        print("Cloning shadow repo...")
        chdir(cloned_repos)
        run_cmd(["git", "clone", remote_url])
        run_cmd(["git", "checkout", branch])
        chdir(main_repo_path)

def install_metrics_tool():
    if os.path.isfile(metrics_exe):
        return
    
    print(f"Metrics.exe not found in {metrics_exe}, installing...")
    run_cmd(["winget", "install", "Microsoft.DotNet.SDK.Preview"])

    if not os.path.isdir(internal_stuff_path):
        os.mkdir(internal_stuff_path)

    chdir(internal_stuff_path)
    run_cmd(["git", "clone", roslyn_github_repo])
    chdir("roslyn")
    run_cmd(["Restore.cmd"])
    chdir("src\\RoslynAnalyzers\\Tools\\Metrics")
    print(f"Make sure you have 'dotnet' on PATH. 'dotnet build' will be used to build Metrics.exe")
    run_cmd(["dotnet", "build", "/m", "/v:m", "/p:Configuration=Release", "Metrics.csproj"])
    chdir(main_repo_path)

def current_repo_hash(target):
    is_solution, target_path = target
    if is_solution:
        target_path = f"s{target_path}"
    else:
        target_path = f"p{target_path}"

    # Calculate a hash reflecting the current state of the repo.
    contents_hash = hashlib.sha256()

    contents_hash.update(str.encode(target_path))

    contents_hash.update(
        run_cmd_checked(["git", "rev-parse", "HEAD"], capture_output=True).stdout
    )
    contents_hash.update(b"\x00")

    # Git can efficiently tell us about changes to tracked files, including
    # the diff of their contents, if you give it enough "-v"s.

    changes = run_cmd_checked(["git", "status", "-v", "-v"], capture_output=True).stdout
    contents_hash.update(changes)
    contents_hash.update(b"\x00")

    # But unfortunately it can only tell us the names of untracked
    # files, and it won't tell us anything about files that are in
    # .gitignore but can still affect the build.

    untracked_files = []

    # First, get a list of all untracked files sans standard exclusions.

    # -o is for getting other (i.e. untracked) files
    # --exclude-standard is to handle standard Git exclusions: .git/info/exclude, .gitignore in each directory,
    # and the user's global exclusion file.
    changes_others = run_cmd_checked(["git", "ls-files", "-o", "--exclude-standard"], capture_output=True).stdout
    changes_lines = iter(ln.strip() for ln in changes_others.split(b"\n"))

    try:
        ln = next(changes_lines)
        while ln:
            untracked_files.append(ln)
            ln = next(changes_lines)
    except StopIteration:
        pass

    # Then, account for some excluded files that we care about.
    untracked_files.extend(GITIGNORED_FILES_THAT_AFFECT_THE_BUILD)

    # Finally, get hashes of everything.
    # Skip files that don't exist, e.g. missing GITIGNORED_FILES_THAT_AFFECT_THE_BUILD. `hash-object` errors out if it gets
    # a non-existent file, so we hope that disk won't change between this filter and the cmd run just below.
    filtered_untracked = [nm for nm in untracked_files if os.path.isfile(nm)]
    if len(filtered_untracked) > 0:
        # Reading contents of the files is quite slow when there are lots of them, so delegate to `git hash-object`.
        git_hash_object_cmd = ["git", "hash-object"]
        git_hash_object_cmd.extend(filtered_untracked)
        changes_untracked = run_cmd_checked(git_hash_object_cmd, capture_output=True).stdout
        contents_hash.update(changes_untracked)
        contents_hash.update(b"\x00")
    
    hash = contents_hash.hexdigest()
    if verbose:
        print(f"Current hash: {hash}")

    return hash

def chdir(path):
    if verbose:
        print(f"{Color.BLUE}chdir {path}{Color.OFF}")

    os.chdir(path)

def run_cmd(*args, **kwargs):
    if verbose:
        print(f"{Color.BLUE}Running cmd: {args}{Color.OFF}")
    
    print(f"{Color.DEFAULT}", end='')
    res = subprocess.run(*args, **kwargs)
    print(f"{Color.OFF}", end='')
    return res

def run_cmd_checked(*args, **kwargs):
    """Run a command, throwing an exception if it exits with non-zero status."""
    kwargs["check"] = True

    if verbose:
        print(f"{Color.BLUE}Running cmd: {args}{Color.OFF}")

    print(f"{Color.DEFAULT}", end='')
    res = subprocess.run(*args, **kwargs)
    print(f"{Color.OFF}", end='')
    return res
