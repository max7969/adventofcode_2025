import day11
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day11/ressources/test') as f:
        content = f.readlines()
        result = day11.compute(content)
        assert result == 5

def test_part1():
    # Open file test and read lines
    with open('./day11/ressources/input') as f:
        content = f.readlines()
        result = day11.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day11/ressources/test2') as f:
        content = f.readlines()
        result = day11.compute2(content)
        assert result == 2

def test_part2():
    # Open file test and read lines
    with open('./day11/ressources/input') as f:
        content = f.readlines()
        result = day11.compute2(content)
        print(result)