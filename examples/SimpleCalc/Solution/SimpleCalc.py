## Simple calculator program using based input from user
from typing import Tuple, Optional, Callable
import sys

# Function to add two numbers
def add(x, y) -> float:
    """Add Function"""
    return x + y


# Function to subtract two numbers
def subtract(x, y) -> float:
    """Subtract Function"""
    return x - y

def multiply(x, y) -> float:
    """Multiply Function"""
    return x * y

def divide(x, y) -> float:
    """Divide Function"""
    return x / y

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
    if func_str == "+":
        return add
    elif func_str == "-":
        return subtract
    elif func_str == "*":
        return multiply
    elif func_str == "/":
        return divide
    else:
        print("Invalid function, please try again. Valid functions are +, -, *, /", file=sys.stderr)
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