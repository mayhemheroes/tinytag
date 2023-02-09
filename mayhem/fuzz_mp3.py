#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports():
    from tinytag import TinyTag

from tinytag.tinytag import TinyTagException
import struct
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        with fdp.ConsumeTemporaryFile('.mp3', all_data=True, as_bytes=True) as tag:
            TinyTag.get(tag)
    except (TinyTagException, struct.error):
        return -1

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
