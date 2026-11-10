# Smart Calculator

A command-line calculator written in Python. This is the final project of Week 1 of my Python challenge.

The program shows a menu of operations, asks for two numbers, prints the result, and lets you keep calculating until you choose to exit.

## Features

- Six operations: addition, subtraction, multiplication, division, power, and modulo
- Works with integers and decimal numbers (inputs are converted to `float`)
- Protection against division by zero (for both `/` and `%`)
- Validation of the selected menu option
- Continuous loop with a "Do you want to continue?" prompt
- Clean, formatted console output

## Requirements

- Python 3.6 or higher (uses f-strings)
- No external libraries

## Getting Started

1. Save the code to a file, for example `calculator.py`.
2. Run it from the terminal:

```bash
python calculator.py
```

## Usage

```
================================
        SMART CALCULATOR
================================

Available operations:

1. Addition        (+)
2. Subtraction     (-)
3. Multiplication (*)
4. Division        (/)
5. Power           (**)
6. Modulo          (%)
7. Exit

================================
Select operation: 4
Enter first number: 10
Enter second number: 4
--------------------------------
Result: 10.0 / 4.0 = 2.5
--------------------------------
Do you want to continue? (yes/no): no
Calculator closed.
```

## How It Works

1. The main `while True` loop keeps the program running.
2. The user selects an operation (`1`-`6`), or `7` to exit.
3. Invalid menu choices print an error and return to the menu.
4. The user enters two numbers.
5. The matching operation is calculated with an `if / elif` chain.
6. Division and modulo check for a zero divisor before calculating.
7. The result is printed, and the user decides whether to continue.

## Error Handling

| Situation | Behavior |
|-----------|----------|
| Menu option outside 1-7 | Prints `Error: Invalid operation!` and shows the prompt again |
| Division or modulo by zero | Prints `Error: Division by zero is not allowed!` |

## Known Limitations

- Entering non-numeric input (e.g. letters) causes a `ValueError` and crashes the program.
- Any answer other than `no` to the continue prompt keeps the calculator running.

## Possible Improvements

- Wrap input in `try / except` to handle invalid values
- Move each operation into its own function
- Add more operations (square root, percentage, floor division)
- Keep a history of calculations

## Concepts Practiced

- Variables and data types
- User input and type conversion
- Conditional statements (`if / elif / else`)
- `while` loops with `break` and `continue`
- f-string formatting
- Basic error handling

## Author

Kubanychbek — Python challenge, Week 1