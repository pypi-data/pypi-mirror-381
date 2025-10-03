#!/usr/bin/env python3
"""
Main entry point for executing metaport as a module.

This allows the package to be executed with:
    python -m metaport [arguments]
"""

import sys
from .metaport import main

if __name__ == '__main__':
    sys.exit(main())
