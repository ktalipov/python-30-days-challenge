print(
    """
================================
        SMART CALCULATOR
================================
"""
)

print(
    """
Available operations:

1. Addition        (+)
2. Subtraction     (-)
3. Multiplication (*)
4. Division        (/)
5. Power           (**)
6. Modulo          (%)
7. Exit
"""
)

print("================================")

while True:
    operation = int(input("Select operation: "))

    if operation == 7:
        print("Calculator closed.")
        break

    if operation not in range(1, 7):
        print("Error: Invalid operation!")
        continue

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    result = None
    operator = ""

    if operation == 1:
        result = number1 + number2
        operator = "+"

    elif operation == 2:
        result = number1 - number2
        operator = "-"

    elif operation == 3:
        result = number1 * number2
        operator = "*"

    elif operation == 4:
        operator = "/"

        if number2 == 0:
            print("Error: Division by zero is not allowed!")
        else:
            result = number1 / number2

    elif operation == 5:
        result = number1 ** number2
        operator = "**"

    elif operation == 6:
        operator = "%"

        if number2 == 0:
            print("Error: Division by zero is not allowed!")
        else:
            result = number1 % number2

    print("--------------------------------")

    if result is not None:
        print(f"Result: {number1} {operator} {number2} = {result}")

    print("--------------------------------")

    is_continue = input(
        "Do you want to continue? (yes/no): "
    ).strip().lower()

    if is_continue == "no":
        print("Calculator closed.")
        break