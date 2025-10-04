import argparse
from .operations import add, subtract, multiply, divide

def main():
    parser = argparse.ArgumentParser(
        description="Perform arithmetic operations on multiple numbers."
    )
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="The operation to perform"
    )
    parser.add_argument(
        "numbers",
        nargs="+",
        type=float,
        help="Numbers to operate on"
    )

    args = parser.parse_args()

    if args.operation == "add":
        result = add(*args.numbers)
    elif args.operation == "subtract":
        result = subtract(*args.numbers)
    elif args.operation == "multiply":
        result = multiply(*args.numbers)
    elif args.operation == "divide":
        result = divide(*args.numbers)
    else:
        parser.error("Invalid operation")

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
