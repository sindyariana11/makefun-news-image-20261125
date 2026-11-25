#!/usr/bin/env python3
"""THE GLOBAL LEDGER — entrypoint (Akun 10, News Image 20261125).

entry.png is the finished page and is not redrawn here. Running
this program copies it, byte for byte, to /output/entry.png.
Standard library only.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    os.makedirs("/output", exist_ok=True)
    dst = os.path.join("/output", "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
