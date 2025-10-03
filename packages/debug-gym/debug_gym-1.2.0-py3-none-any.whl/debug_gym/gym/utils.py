import codecs
import os
import re
import shutil
import tempfile
import zipfile
from os.path import join as pjoin
from pathlib import Path
from typing import Any, Callable

import requests
from tqdm import tqdm


def filter_non_utf8(text):
    """Filter out non-UTF-8 characters from text."""
    if not text:
        return None
    if isinstance(text, str):
        return text.encode("utf-8", errors="ignore").decode("utf-8")
    return text


def show_line_number(code_string, code_path=None, environment=None, start_index=1):
    # Show line number for each line
    # code_path is the path of the code file in view
    # environment where to find the breakpoints state
    # start_index is the starting line number for the code string
    # line numbers are 1-indexed, and are separated from the code by a space

    assert code_string, "code_string should not be empty"
    assert isinstance(
        code_string, str
    ), f"code_string should be a string, but got {type(code_string)}"
    code_line = code_string.split("\n")

    output = []
    # Calculate the number of digits needed for line numbers
    # e.g., 999 lines -> 4 digits
    # 1-4 digits: 4
    # 5-8 digits: 8...
    line_number_digit = len(str(start_index + len(code_line) + 1))
    line_number_digit = (line_number_digit - 1) // 4 * 4 + 4
    for i, line in enumerate(code_line):
        has_breakpoint = False
        line_number = start_index + i
        if code_path is not None and environment is not None:
            has_breakpoint = environment.has_breakpoint(code_path, line_number)
        _tmp = ""
        if has_breakpoint:
            _tmp += "B"
        _tmp = "{:<2}{:>{}} {}".format(_tmp, line_number, line_number_digit, line)
        output.append(_tmp)
    return "\n".join(output)


def make_file_matcher(
    base_dir: str | Path,
    pattern_files: list[str | Path] | str | Path,
    patterns: list[str] | None = None,
) -> Callable[[str | Path], bool]:
    """
    Creates a file matcher function based on ignore patterns from files and additional patterns.

    Args:
        base_dir (str | Path): The base directory to normalize the patterns against.
        pattern_files (list[str | Path] | str | Path): Path(s) to file(s) containing gitignore-like patterns.
        patterns (list[str]): Additional patterns to include. Defaults to an empty list.

    Returns:
        function: A function that takes a file path as input and returns True if the file matches any of the patterns, False otherwise.
    """
    # Ref: gitignore_parser.parse_gitignore
    from gitignore_parser import _normalize_path, handle_negation, rule_from_pattern

    if patterns is None:
        patterns = []

    if isinstance(pattern_files, (str, Path)):
        pattern_files = [pattern_files]

    # iterate over all pattern files and read their contents
    lines = []
    for pattern_file in pattern_files:
        pattern_file = Path(pattern_file)
        if pattern_file.is_file():
            with open(pattern_file) as ignore_file:
                lines.extend(ignore_file.readlines())

    # concatenate the additional patterns
    lines += patterns

    base_dir = _normalize_path(str(Path(base_dir)))
    rules = []
    for i, line in enumerate(lines):
        line = line.rstrip("\n")
        rule = rule_from_pattern(line.rstrip("\n"), base_dir, ("multiple_files", i))
        if rule:
            rules.append(rule)

    if not any(r.negation for r in rules):
        return lambda file_path: any(r.match(file_path) for r in rules)
    else:
        # We have negation rules. We can't use a simple "any" to evaluate them.
        # Later rules override earlier rules.
        return lambda file_path: handle_negation(file_path, rules)


def create_ignore_file(
    filepath: str | Path, patterns: list[str] = [], include_gitignore: bool = True
):
    """
    Creates a file at the specified `filepath` containing gitignore-like patterns.

    Files and directories matching the patterns in that file will be treated differently.
    E.g., Files in a `.debugignore` file will be ignored by the environment.
          Files in a `.debugreadonly` file will be marked as readonly.

    Args:
        filepath (str): The file path where to create the ignore file.
        patterns (list[str]): A list of patterns to include in the ignore file.
        include_gitignore (bool): If True, includes the contents of an existing .gitignore file
                                  in the ignore file. Default is True.
    """
    path = Path(filepath)
    gitignore_file = path.parent / ".gitignore"
    if include_gitignore and gitignore_file.exists():
        with open(gitignore_file) as f:
            patterns = patterns + f.read().splitlines()

    with open(path, "w") as f:
        f.write("\n".join(patterns + [path.name]))


def _walk(path, depth: int | None = None, skip: Callable | None = None):
    """recursively list files and directories up to a certain depth"""
    depth = 1e5 if depth is None else depth
    if depth <= 0:  # stop recursion
        return

    with os.scandir(path) as p:
        for entry in sorted(p, key=lambda x: x.name):
            if skip and skip(entry.path):
                continue

            yield Path(entry)
            if entry.is_dir() and depth > 0:
                yield from _walk(entry.path, depth=depth - 1, skip=skip)


def is_subdirectory(path, directory):
    directory = str(directory)
    if not path.startswith(directory):
        path = pjoin(directory, path)
    return not os.path.relpath(path, directory).startswith("..")


def cleanup_pytest_output(output):
    # Remove timing, root dir, and platform to avoid randomizing LLM's response.
    res = re.sub(
        r"^Ran \d+ tests? in \d+\.\d+s$",
        "",
        output,
        flags=re.MULTILINE,
    )
    res = re.sub(r"^====*$", "====", res, flags=re.MULTILINE)
    res = re.sub(r"^----*$", "----", res, flags=re.MULTILINE)
    res = re.sub(r"^platform .*\n", "", res, flags=re.MULTILINE)
    res = re.sub(r"^rootdir: .*\n", "", res, flags=re.MULTILINE)
    res = re.sub(r"^plugins: .*\n", "", res, flags=re.MULTILINE)
    res = re.sub(r"^cachedir: .*\n", "", res, flags=re.MULTILINE)

    return res


def extract_max_score_from_pytest_output(output):
    # ... collected 25 items
    # ... collected 1 item
    match = re.search(r"collected (\d+) items?", output)
    if match:
        return max(int(match.group(1)), 1.0)
    else:
        raise ValueError("Cannot extract max score from pytest output.", output)


def extract_reward_from_pytest_output(output):
    # We extract the number of tests passed from the pytest output.
    # The number of tests passed is the reward.
    # e.g. ========================= 25 failed in 0.06s =========================
    # e.g. ========================= 23 failed, 2 passed in 0.06s =========================
    match = re.search(r"(\d+) passed", output)
    if match:
        return int(match.group(1))

    return 0


def filter_problems(
    dataset: dict[str, Any],
    problems: str | list[str] | None = None,
    custom_splits: dict[str, Any] | None = None,
    excluded_ids: list[str] | None = None,
) -> dict[str, Any]:
    excluded_ids = excluded_ids or []
    custom_splits = custom_splits or {}
    problems = "all" if problems is None else problems

    if not isinstance(problems, str):
        # Check that all problems are valid task names.
        for problem in problems:
            if problem not in dataset:
                raise ValueError(
                    f"Invalid problem id: '{problem}'.\nChoose from: {sorted(dataset)}"
                )

        # Make sure all problems are unique.
        if len(problems) != len(set(problems)):
            raise ValueError("Duplicate problem IDs found in the list.")

        return problems  # Assuming a list of problem IDs.

    if problems == "all":
        return [k for k in dataset if k not in excluded_ids]
    elif problems in dataset:
        return [problems]  # Single task
    elif problems in custom_splits:
        return custom_splits[problems]
    else:
        raise ValueError(
            f"Invalid split or problem id: '{problems}'.\nChoose from: {sorted(dataset) + ['all'] + sorted(custom_splits)}"
        )


def mkdirs(dirpath: str) -> str:
    """Create a directory and all its parents.

    If the folder already exists, its path is returned without raising any exceptions.

    Arguments:
        dirpath: Path where a folder need to be created.

    Returns:
        Path to the (created) folder.
    """
    try:
        os.makedirs(dirpath)
    except FileExistsError:
        pass

    return dirpath


def download(url, dst, desc=None, force=False):
    """Download a remote file using HTTP get request.

    Args:
        url (str): URL where to get the file.
        dst (str): Destination folder where to save the file.
        force (bool, optional):
            Download again if it exists]. Defaults to False.

    Returns:
        str: Path to the downloaded file.

    Notes:
        This code is inspired by
        https://github.com/huggingface/transformers/blob/v4.0.0/src/transformers/file_utils.py#L1069
    """
    filename = url.split("/")[-1]
    path = pjoin(mkdirs(dst), filename)

    if os.path.isfile(path) and not force:
        return path

    # Download to a temp folder first to avoid corrupting the cache
    # with incomplete downloads.
    temp_dir = mkdirs(pjoin(tempfile.gettempdir(), "tales"))
    temp_path = pjoin(temp_dir, filename)
    with open(temp_path, "ab") as temp_file:
        headers = {}
        resume_size = temp_file.tell()
        if resume_size:
            headers["Range"] = f"bytes={resume_size}-"
            headers["x-ms-version"] = "2020-04-08"  # Needed for Range support.

        r = requests.get(url, stream=True, headers=headers)
        if r.headers.get("x-ms-error-code") == "InvalidRange" and r.headers[
            "Content-Range"
        ].rsplit("/", 1)[-1] == str(resume_size):
            shutil.move(temp_path, path)
            return path

        r.raise_for_status()  # Bad request.
        content_length = r.headers.get("Content-Length")
        total = resume_size + int(content_length)
        pbar = tqdm(
            unit="B",
            initial=resume_size,
            unit_scale=True,
            total=total,
            desc=desc or "Downloading {}".format(filename),
            leave=False,
        )

        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                pbar.update(len(chunk))
                temp_file.write(chunk)

    shutil.move(temp_path, path)

    pbar.close()
    return path


def unzip(filename, dst=None, force=False):
    zipped_file = zipfile.ZipFile(filename)
    filenames_to_extract = list(zipped_file.namelist())
    dst = dst or os.path.dirname(filename)

    desc = f"Extracting {os.path.basename(filename)}"
    skipped = 0
    for f in tqdm(filenames_to_extract, desc=desc, leave=False, unit="file"):
        if not os.path.isfile(pjoin(dst, f)) or force:
            zipped_file.extract(f, dst)
        else:
            skipped += 1

    if skipped:
        print(f"{skipped} files skipped (use -f to overwrite).")
