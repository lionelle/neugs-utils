from typing import Tuple, Optional, Callable
import sys

## Assume being stuck on an island and not allowed to step on surrounding seas
## Write a program that checks for top, bottom, left and right boundaries on the island grid 

## Example: grid = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]] 
## 0's represents sea, 1's represents land and (row,col) is the current location on the island

# Function to check a top out-of-bounds error on the grid
def can_move_north(grid, row, col) -> bool:
    """Move-up Function"""
    if grid[row-1, col] == 0:
        print('This is the North boundary, thou shall not flee the island!')
        return False
    return True

# Function to check a bottom out-of-bounds error on the grid
def can_move_south(grid, row, col) -> bool:
    """Move-down Function"""
    if grid[row+1, col] == 0:
        print('This is the South boundary, thou shall not flee the island!')
        return False
    return True

# Function to check a left out-of-bounds error on the grid
def can_move_west(grid, row, col) -> bool:
    """Move-left Function"""
    if grid[row, col-1] == 0:
        print('This is the West boundary, thou shall not flee the island!')
        return False
    return True

# Function to check a right out-of-bounds error on the grid
def can_move_east(grid, row, col) -> bool:
    """Move-right Function"""
    if grid[row, col+1] == 0:
        print('This is the East boundary, thou shall not flee the island!')
        return False
    return True

def get_client_input() -> Optional[Tuple[str, float, float]]:
    """Gets the clients input, and which function to use, in post script notation"""
    input_str = input("> ")
    if input_str == "exit":
        return None
    input_list = input_str.split(" ")

    if len(input_list) != 3:
        print("Invalid input, please try again. Format should be > <function> <num1> <num2>", file=sys.stderr)
        return get_client_input()
    try:
        return input_list[0], float(input_list[1]), float(input_list[2])
    except ValueError:
        print("Invalid input, please try again. Format should be > <function> <num1> <num2>", file=sys.stderr)
        return get_client_input()

def select_function(func_str: str) -> Optional[Callable[[float, float], float]]:
    """Selects the function to use based on the string passed in"""
    if func_str == "N":
        return can_move_north
    elif func_str == "S":
        return can_move_south
    elif func_str == "W":
        return can_move_west
    elif func_str == "E":
        return can_move_east
    else:
        print("Invalid function, please try again. Valid functions are N, S, W, E", file=sys.stderr)
        return None

def main():
    """Main function"""
    while True:
        input_tuple = get_client_input()
        if input_tuple is None:
            break
        func = select_function(input_tuple[0])
        if func is None:
            continue
        print("Answer: " + str(func(input_tuple[1], input_tuple[2])))
    


if __name__ == "__main__":
    main()