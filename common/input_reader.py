"""Input reading utilities for Advent of Code solutions."""
import os
from typing import List, Any, Callable


def read_input(solution_file: str, test: bool = False) -> List[str]:
    """Read the input file for a given solution.
    
    Args:
        solution_file: The __file__ variable from the solution
        test: If True, read from test file instead of input file
    
    Returns:
        List of strings, one per line from the input file
    """
    dir_path = os.path.dirname(os.path.abspath(solution_file))
    file_name = "test" if test else "input"
    file_path = os.path.join(dir_path, "resources", file_name)
    
    with open(file_path, 'r') as f:
        return f.readlines()


def parse_grid(content: List[str]) -> List[List[str]]:
    """Parse a grid from input content.
    
    Args:
        content: List of strings representing grid rows
    
    Returns:
        2D list representing the grid
    """
    return [list(line.strip()) for line in content]


def parse_numbers(content: List[str], separator: str = None) -> List[List[int]]:
    """Parse numbers from input content.
    
    Args:
        content: List of strings containing numbers
        separator: Optional separator between numbers (None for space)
    
    Returns:
        List of lists of integers
    """
    result = []
    for line in content:
        if separator:
            nums = line.strip().split(separator)
        else:
            nums = line.strip().split()
        result.append([int(n) for n in nums if n])
    return result


def parse_blocks(content: List[str]) -> List[List[str]]:
    """Parse content separated by blank lines into blocks.
    
    Args:
        content: List of strings with blank line separators
    
    Returns:
        List of lists of strings, each sublist is a block
    """
    blocks = []
    current_block = []
    
    for line in content:
        if line.strip():
            current_block.append(line.strip())
        elif current_block:
            blocks.append(current_block)
            current_block = []
            
    if current_block:
        blocks.append(current_block)
        
    return blocks 