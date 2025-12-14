import day12
import pytest

def test_part1():
    # Open file test and read lines
    with open('./day12/ressources/input') as f:
        content = f.readlines()
        result = day12.compute(content)
        print(result)
