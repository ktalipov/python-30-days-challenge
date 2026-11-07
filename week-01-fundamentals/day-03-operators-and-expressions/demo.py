# demo.py — simple demo of Python operators and expressions

# Arithmetic
a, b = 7, 2
print("Arithmetic:")
print(f"  {a} + {b}  = {a + b}")
print(f"  {a} / {b}  = {a / b}")
print(f"  {a} // {b} = {a // b}")
print(f"  {a} % {b}  = {a % b}")
print(f"  {a} ** {b} = {a ** b}")
print(f"  -7 // 2 = {-7 // 2}  (floor division rounds down)")

# Comparison and chaining
x = 5
print("\nComparison:")
print(f"  1 < {x} < 10 -> {1 < x < 10}")
print(f"  {x} == 5.0   -> {x == 5.0}")

# Logical operators (short-circuit, return operands)
print("\nLogical:")
print(f"  0 or 'default'  -> {0 or 'default'!r}")
print(f"  3 and 5         -> {3 and 5}")
print(f"  not []          -> {not []}")

# Floating-point precision
import math
print("\nFloats:")
print(f"  0.1 + 0.2 == 0.3          -> {0.1 + 0.2 == 0.3}")
print(f"  math.isclose(0.1+0.2, 0.3) -> {math.isclose(0.1 + 0.2, 0.3)}")

# Membership and identity
nums = [1, 2, 3]
print("\nMembership / identity:")
print(f"  2 in {nums}     -> {2 in nums}")
print(f"  'ban' in 'banana' -> {'ban' in 'banana'}")
value = None
print(f"  value is None     -> {value is None}")

# Ternary
age = 20
status = "adult" if age >= 18 else "minor"
print(f"\nTernary: age={age} -> {status}")

# Walrus operator
items = [1, 2, 3, 4]
if (n := len(items)) > 3:
    print(f"Walrus: list has {n} items")

# Bitwise
p, q = 6, 3
print("\nBitwise:")
print(f"  {p} & {q} = {p & q}")
print(f"  {p} | {q} = {p | q}")
print(f"  {p} ^ {q} = {p ^ q}")
print(f"  {p} << 1 = {p << 1}")
