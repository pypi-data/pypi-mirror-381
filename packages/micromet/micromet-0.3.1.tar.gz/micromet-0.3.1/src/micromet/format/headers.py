from __future__ import annotations
from pathlib import Path
import csv
import re
import pandas as pd
from collections import defaultdict


# ──────────────────────────────────────────────────────────────────────────────
# 1.  Tiny helpers
# ──────────────────────────────────────────────────────────────────────────────
def looks_like_header(line: str, alpha_thresh: int = 1) -> bool:
    """
    Heuristically determine if a line appears to be a header.

    This function checks if a line from a text file is likely to be a
    header row by checking for the presence of alphabetic characters.

    Parameters
    ----------
    line : str
        A single line of text from a file.
    alpha_thresh : int, optional
        The minimum number of alphabetic fields required to be
        considered a header. Defaults to 1.

    Returns
    -------
    bool
        True if the line is likely a header, False otherwise.
    """
    # line_list = line.split(",")
    # return bool(re.search(r"[A-Za-z]", line_list[0]))

    # ignore empty/whitespace lines
    if not line.strip():
        return False
    sample = line.replace('"', "")  # ignore surrounding quotes
    tokens = sample.split(",")
    n_alpha = sum(bool(re.search("[A-Za-z]", t)) for t in tokens[:5])
    if len(tokens[:5]) and n_alpha / len(tokens[:5]) >= alpha_thresh:
        return True
    # Let csv.Sniffer decide on tougher cases
    try:
        return csv.Sniffer().has_header(sample)
    except csv.Error:
        return False


def sniff_delimiter(path: Path, sample_bytes: int = 2048, default: str = ",") -> str:
    """
    Infer the most likely delimiter used in a text file.

    This function reads a sample from the beginning of a file and uses
    `csv.Sniffer` to detect the delimiter.

    Parameters
    ----------
    path : Path
        The path to the file.
    sample_bytes : int, optional
        The number of bytes to read for the sample. Defaults to 2048.
    default : str, optional
        The delimiter to return if detection fails. Defaults to ",".

    Returns
    -------
    str
        The detected or default delimiter.
    """
    with path.open("r", newline="", encoding="utf-8") as fh:
        sample = fh.read(sample_bytes)
    try:
        return csv.Sniffer().sniff(sample).delimiter
    except csv.Error:
        return default


def _strip_quotes(tokens: list[str]) -> list[str]:
    """
    Remove surrounding quotes from a list of strings.

    Parameters
    ----------
    tokens : list[str]
        A list of strings that may have surrounding quotes.

    Returns
    -------
    list[str]
        The list of strings with quotes removed.
    """
    return [t.strip('"') for t in tokens]


def read_colnames(path: Path) -> list[str]:
    """
    Read column names from the first line of a file.

    This function infers the delimiter, reads the first line of the
    file, and returns the column names.

    Parameters
    ----------
    path : Path
        The path to the file.

    Returns
    -------
    list[str]
        A list of column names.
    """
    delim = sniff_delimiter(path)
    # with path.open(encoding="utf-8") as fh:
    #    first = fh.readline().rstrip("\n\r").split(delim)
    # return _strip_quotes(first)
    delim = sniff_delimiter(path)
    with path.open("rb") as fh:  # read binary
        first = fh.readline().lstrip(b"\xef\xbb\xbf").decode()  # drop BOM
    tokens = first.rstrip("\r\n").split(delim)
    return [t.strip('"') for t in tokens]


def patch_file(
    donor: Path,
    target: Path,
) -> pd.DataFrame:
    """
    Apply a header from a donor file to a target file.

    This function reads the header from a `donor` file and applies it
    to a `target` file that is assumed to be missing a header. The
    modified data is returned as a DataFrame and written back to the
    target file.

    Parameters
    ----------
    donor : Path
        The path to the file with the correct header.
    target : Path
        The path to the file that needs a header.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the data from the target file with the
        new header.
    """
    cols = read_colnames(donor)
    delim = sniff_delimiter(donor)

    df = pd.read_csv(target, header=None, names=cols, delimiter=delim)

    # if write_back:
    #    bak = target.with_suffix(target.suffix + ".bak")
    #    target.replace(bak)
    df.to_csv(target, index=False, sep=delim, quoting=csv.QUOTE_NONE, escapechar="\\")
    return df


# ──────────────────────────────────────────────────────────────────────────────
# 2.  Main routine
# ──────────────────────────────────────────────────────────────────────────────
def fix_all_in_parent(parent: Path, searchstr: str = "*_AmeriFluxFormat_*.dat") -> None:
    """
    Recursively scan a parent directory for files with duplicate names and fix missing headers.

    This function searches `parent` for files matching a given pattern. If duplicate
    filenames are found such that one version has a header and another does not,
    the header is copied from the former to the latter. The target files are
    overwritten in-place, and a `.bak` backup is created for each.

    Parameters
    ----------
    parent : Path
        Root directory to scan for matching files. All subdirectories are included recursively.
    searchstr : str, optional
        Glob-style pattern to match filenames (default is "*_AmeriFluxFormat_*.dat").

    Returns
    -------
    None

    Notes
    -----
    - Files are grouped by basename and inspected line-by-line to determine whether
      they contain a header.
    - If multiple files have headers, only the first one is used as the donor.
    - Files with no header and no matching header source are skipped.

    See Also
    --------
    apply_header : Applies a header from one file to another.
    looks_like_header : Determines whether a line appears to be a valid header.
    patch_file : Wrapper to apply a header to a target file and optionally save it.
    """

    # ------------------------------------------------------------------ #
    # 1. Collect every file path, grouped by basename.
    paths_by_name: dict[str, list[Path]] = defaultdict(list)
    glob_pattern = searchstr
    for p in parent.rglob(glob_pattern):
        if p.is_file():
            paths_by_name[p.name].append(p)

    # ------------------------------------------------------------------ #
    # 2. Examine each group of duplicates
    for fname, paths in paths_by_name.items():
        if len(paths) < 2:
            continue  # no duplicates → nothing to do

        # Classify each copy
        header_files, noheader_files = [], []
        for p in paths:
            first = p.open("r", encoding="utf-8").readline()
            if looks_like_header(first):
                header_files.append(p)
            else:
                noheader_files.append(p)

        if not header_files or not noheader_files:
            # Either (a) every copy already has a header, or (b) none do
            # In both situations we cannot (or need not) patch automatically.
            continue

        # Use the first header-bearing file as the “donor” for all others
        donor = header_files[0]
        for tgt in noheader_files:
            df_fixed = patch_file(donor, tgt)
            print(
                f"[INFO]  Patched  {tgt.relative_to(parent)}   "
                f"({len(df_fixed):,d} rows)"
            )

    print("\n✔ All possible files have been checked.")
    return paths_by_name  # type: ignore


def apply_header(
    header_file: Path,
    target_file: Path,
    *,
    inplace: bool = False,
) -> pd.DataFrame:
    """
    Apply a header from a reference file to a data file and return a DataFrame.

    This function reads column names from `header_file` and applies them to
    `target_file`, which is assumed to lack a header row. The result is returned
    as a pandas DataFrame. Optionally, the function can overwrite `target_file`
    with the updated version, keeping a backup as `*.bak`.

    Parameters
    ----------
    header_file : Path
        Path to the file containing the correct column headers.
    target_file : Path
        Path to the file that is missing column headers.
    inplace : bool, optional
        If True, the modified DataFrame is written back to `target_file`,
        and a backup of the original file is saved with a `.bak` extension.
        Default is False.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the contents of `target_file` with headers applied
        from `header_file`.

    Notes
    -----
    The delimiter is inferred using a sniffing function to ensure consistent parsing
    between the header and target files.
    """
    delimiter = sniff_delimiter(header_file)

    # ------------------------------------------------------------------ #
    # get column names from the good file
    cols = read_colnames(header_file)

    # ------------------------------------------------------------------ #
    # read the data-only file, telling pandas “there is *no* header here”
    df = pd.read_csv(target_file, header=None, names=cols, delimiter=delimiter)

    # ------------------------------------------------------------------ #
    # optionally write the fixed file back to disk
    if inplace:
        backup = target_file.with_suffix(target_file.suffix + ".bak")
        target_file.replace(backup)  # keep a backup
        df.to_csv(target_file, index=False, sep=delimiter)

    return df


def fix_directory_pairs(dir_with_headers: Path, dir_without_headers: Path) -> None:
    """
    Apply headers from a directory of correctly formatted files to a directory
    of files missing headers.

    This function loops through all files in `dir_without_headers`. For each file
    that lacks a header, it attempts to find a matching file by name in
    `dir_with_headers` and uses it to patch the missing header. The original file
    is overwritten, and a `.bak` backup is created.

    Parameters
    ----------
    dir_with_headers : Path
        Directory containing files with valid headers.
    dir_without_headers : Path
        Directory containing files that may be missing headers.

    Returns
    -------
    None

    Notes
    -----
    This function assumes that files in both directories are named identically,
    and that headers can be determined by inspecting the first line of each file.

    See Also
    --------
    apply_header : Applies a header from one file to another.
    """
    # index the header-bearing directory for O(1) lookup
    header_index = {p.name: p for p in dir_with_headers.iterdir() if p.is_file()}

    for f in dir_without_headers.iterdir():
        if not f.is_file():
            continue

        # Fast header check: read only the first line
        first_line = f.open("r", encoding="utf-8").readline()
        if looks_like_header(first_line):
            continue  # nothing to do

        if f.name not in header_index:
            print(f"[WARN] No header twin found for {f}")
            continue

        df_fixed = apply_header(header_index[f.name], f, inplace=True)
        print(f"[INFO] Patched header on {f} ({len(df_fixed)} rows)")
