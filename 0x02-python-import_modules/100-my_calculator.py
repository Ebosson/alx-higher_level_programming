#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Define the available operators and check if the provided operator is valid
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Extract the numerical values from command-line arguments
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # Perform the arithmetic operation and print the result
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))

