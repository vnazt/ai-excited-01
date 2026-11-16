"""Deliver the entry image for the make.fun ai-excited-01 bounty.

This entry is judged on a single picture, stored beside this file as
``entry.png``.  The program's one job is to hand that picture to the
trial harness untouched: it copies the file, byte for byte, into the
output directory.  Because nothing is decoded or re-encoded, repeated
runs always produce identical output, as the competition requires.

The output directory is read from the ``MAKEFUN_OUTPUT_DIR``
environment variable (``/output`` when unset) and is created first if
it does not exist yet, so the copy cannot fail on a missing folder.
"""

import os
import shutil

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def destination() -> str:
    """Return where the image copy goes, creating the folder if needed."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, SOURCE_NAME)


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(os.path.join(here, SOURCE_NAME), destination())


if __name__ == "__main__":
    main()
