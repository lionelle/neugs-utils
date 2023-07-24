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

##def get_client_input() 
   

##def select_function(func_str: str) 
    """Selects the function to use based on the string passed in"""
   

def main():
    """Main function"""
    



if __name__ == "__main__":
    main()