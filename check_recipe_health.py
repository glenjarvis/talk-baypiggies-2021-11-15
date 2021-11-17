#!/usr/bin/env python

"""Health Checker

I will complain if your recipes have bad stuff in them.
"""

from pathlib import Path
import sys

BAD_INGREDIENTS = {
    "butter": -1,
    "salt": -2,
    "sugar": -3,
}

for p in Path('./recipes').glob('*.txt'):
    if "butter" in p.read_text():
        print(f"Recipe {p.name} contains butter!")
        sys.exit(-1)
