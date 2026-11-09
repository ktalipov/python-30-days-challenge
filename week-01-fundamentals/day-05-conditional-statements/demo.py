# demo.py — simple demo of conditional statements

# if / else
age = 20
if age >= 18:
    print("if/else: Adult")
else:
    print("if/else: Minor")

# if / elif / else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"elif: score {score} -> grade {grade}")

# Logical operators
has_ticket = True
if age >= 18 and has_ticket:
    print("and: Enter")

day = "Sat"
if day == "Sat" or day == "Sun":
    print("or: Weekend")

# Membership
color = "green"
if color in ("red", "green", "blue"):
    print(f"in: {color} is a primary color")

# Chained comparison
x = 5
if 1 < x < 10:
    print("chain: 1 < x < 10")

# Truthiness
items = []
if not items:
    print("truthy: list is empty")

name = ""
print(f"truthy: name = {name or 'Guest'!r}")

# is None vs falsy 0
count = 0
if count is not None:
    print("is not None: count has a value (even 0)")
if not count:
    print("falsy: but 0 is falsy")

# Short-circuit
d = 0
if d != 0 and 10 / d > 2:
    print("never printed")
else:
    print("short-circuit: no ZeroDivisionError")

# Nested vs flat
has_license = True
if age >= 18 and has_license:
    print("flat: Can drive")


# Guard clauses
def process(user):
    if user is None:
        return "No user"
    if not user.get("active"):
        return "Inactive"
    return "OK"


print("guard:", process(None), "|", process({"active": False}), "|", process({"active": True}))

# Ternary
status = "adult" if age >= 18 else "minor"
print(f"ternary: {status}")
n = 3
print(f"ternary: You have {n} item{'s' if n != 1 else ''}")

# match / case (Python 3.10+)
command = "stop"
match command:
    case "start":
        print("match: Starting")
    case "stop":
        print("match: Stopping")
    case "pause" | "wait":
        print("match: Pausing")
    case _:
        print("match: Unknown command")

point = (3, 3)
match point:
    case (0, 0):
        print("match: Origin")
    case (x, 0):
        print(f"match: On X axis at {x}")
    case (x, y) if x == y:
        print("match: Diagonal")
    case (x, y):
        print(f"match: Point {x}, {y}")

response = {"status": 200, "data": "hello"}
match response:
    case {"status": 200, "data": data}:
        print(f"match: data = {data}")
    case {"status": 404}:
        print("match: Not found")

# FizzBuzz
print("FizzBuzz:", end=" ")
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# Leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"leap year: {year} is a leap year")
