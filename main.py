"""Entry program for the make.fun ai-excited-01 bounty.

Copies the entry image (entry.png, stored beside this file) into the
trial's output directory, byte for byte. The output directory comes
from the MAKEFUN_OUTPUT_DIR environment variable when set, and falls
back to /output otherwise.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def source_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, IMAGE_NAME)


def target_path():
    out_dir = os.environ.get(OUTPUT_ENV_VAR) or DEFAULT_OUTPUT_DIR
    return out_dir, os.path.join(out_dir, IMAGE_NAME)


def main():
    src = source_path()
    if not os.path.isfile(src):
        print(f"error: {IMAGE_NAME} not found next to main.py", file=sys.stderr)
        return 1
    out_dir, dst = target_path()
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    print(f"copied {src} -> {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
