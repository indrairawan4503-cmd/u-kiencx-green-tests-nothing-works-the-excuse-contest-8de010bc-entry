"""Green Tests, Nothing Works entry (variant B, v8 final line): the README-only test suite.

Writes exactly one funny line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
The line is the v8 final: all 412 tests green because every one of them runs
against the README, and the README has never had a bug.

Gate self-check: before anything is written, ENTRY_TEXT must be 1..MAX_CHARS
characters (MAX_CHARS = 140, the competition cap). A text outside that range
raises ValueError and nothing is written, so a bad line can never reach the
grader. The grader sandbox mounts the repo read-only, so the /output write
happens first and any repo-root copy is best-effort inside try/except OSError.
"""

import os

ENTRY_TEXT = (
    "All 412 tests green: every one runs against the README, and the README "
    "has never had a bug. Deploying."
)

MAX_CHARS = 140


def check_entry_text() -> None:
    """Raise ValueError unless ENTRY_TEXT is a valid 1..MAX_CHARS-char line."""
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS:
        raise ValueError(
            f"ENTRY_TEXT must be 1..{MAX_CHARS} chars, got {len(ENTRY_TEXT)}"
        )
    if not ENTRY_TEXT.strip():
        raise ValueError("ENTRY_TEXT must not be only whitespace")


def get_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir: str) -> None:
    check_entry_text()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


def copy_to_repo_root() -> None:
    try:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(repo_root, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


def main() -> None:
    check_entry_text()
    write_entry(get_output_dir())
    copy_to_repo_root()


if __name__ == "__main__":
    main()
