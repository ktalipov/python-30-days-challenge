# Operators and Expressions in Python

## Introduction

An **expression** is a combination of values, variables, operators, and function calls that Python evaluates to a single value. An **operator** is a symbol or keyword that performs an operation on one or more **operands**.

```python
2 + 3 * 4        # expression -> 14
x = 5            # statement (assignment), not an expression
```

**Expression vs. statement:**

|**Feature**|**Expression**|**Statement**|
|---|---|---|
|**Produces**|A value|An action (no value)|
|**Examples**|`1 + 2`, `len(s)`, `a if b else c`|`x = 1`, `if`, `for`, `import`, `del`|
|**In REPL**|Result is printed|Nothing is printed|

**Operator types by number of operands:**

- **Unary** — one operand: `-x`, `not x`, `~x`.
- **Binary** — two operands: `a + b`, `a and b`.
- **Ternary** — three operands: `a if cond else b`.

---

## Arithmetic Operators

|**Operator**|**Name**|**Example**|**Result**|
|---|---|---|---|
|`+`|Addition|`7 + 2`|`9`|
|`-`|Subtraction|`7 - 2`|`5`|
|`*`|Multiplication|`7 * 2`|`14`|
|`/`|True division|`7 / 2`|`3.5`|
|`//`|Floor division|`7 // 2`|`3`|
|`%`|Modulo (remainder)|`7 % 2`|`1`|
|`**`|Exponentiation|`7 ** 2`|`49`|

**Key points:**

- `/` **always** returns a `float`, even for `6 / 2` -> `3.0`.
- `//` rounds toward **negative infinity** (floor), not toward zero.
- `%` result has the **same sign as the divisor**.
- `a == (a // b) * b + a % b` always holds.

```python
-7 // 2     # -4  (floor, not -3)
-7 % 2      # 1   (sign of divisor)
7 % -2      # -1
divmod(7, 2)   # (3, 1) — quotient and remainder at once
pow(2, 10)     # 1024
pow(2, 10, 7)  # 2 — (2**10) % 7, efficient modular power
```

**Unary operators:**

```python
+x      # unary plus
-x      # negation
```

**Other notes:**

- `**` is right-associative: `2 ** 3 ** 2` = `2 ** 9` = `512`.
- `-2 ** 2` = `-4` because `**` binds tighter than unary minus.
- `ZeroDivisionError` is raised by `/`, `//`, and `%` when the divisor is `0`.
- `+` and `*` also work on sequences: `"ab" + "cd"`, `"ab" * 3`, `[1] * 3`.

### Floating-Point Precision

Floats are stored in binary, so some decimals cannot be represented exactly.

```python
0.1 + 0.2            # 0.30000000000000004
0.1 + 0.2 == 0.3     # False
```

```python
import math
math.isclose(0.1 + 0.2, 0.3)    # True

from decimal import Decimal
Decimal("0.1") + Decimal("0.2")  # Decimal('0.3')
```

- Never compare floats with `==`; use `math.isclose()`.
- Use `decimal.Decimal` for money.

---

## Comparison Operators

Comparison operators return a `bool` (`True` / `False`).

|**Operator**|**Meaning**|**Example**|
|---|---|---|
|`==`|Equal to|`3 == 3.0` -> `True`|
|`!=`|Not equal to|`3 != 4` -> `True`|
|`>`|Greater than|`5 > 2`|
|`<`|Less than|`2 < 5`|
|`>=`|Greater than or equal to|`5 >= 5`|
|`<=`|Less than or equal to|`4 <= 5`|

### Chained Comparisons

Python allows mathematical-style chaining.

```python
x = 5
1 < x < 10          # True  (same as 1 < x and x < 10)
1 < x < 3 < 100     # False
a == b == c         # all three equal
```

- Each operand is evaluated **once**.
- Evaluation short-circuits at the first `False`.

### Comparing Different Types

```python
1 == 1.0          # True
1 == "1"          # False
1 < "a"           # TypeError (no ordering between int and str)
"apple" < "banana"   # True (lexicographic)
[1, 2] < [1, 3]      # True (element by element)
(1, 2) == (1, 2)     # True
```

---

## Logical Operators

|**Operator**|**Meaning**|**Example**|
|---|---|---|
|`and`|`True` if **both** are truthy|`a > 0 and b > 0`|
|`or`|`True` if **at least one** is truthy|`a > 0 or b > 0`|
|`not`|Inverts the truth value|`not a`|

**Truth table:**

|`a`|`b`|`a and b`|`a or b`|`not a`|
|---|---|---|---|---|
|`True`|`True`|`True`|`True`|`False`|
|`True`|`False`|`False`|`True`|`False`|
|`False`|`True`|`False`|`True`|`True`|
|`False`|`False`|`False`|`False`|`True`|

### Truthy and Falsy Values

**Falsy** (evaluate to `False` in a boolean context):

- `False`, `None`
- Zero: `0`, `0.0`, `0j`
- Empty collections: `""`, `[]`, `()`, `{}`, `set()`, `range(0)`

**Everything else is truthy.**

```python
bool(0)        # False
bool("")       # False
bool([0])      # True  (non-empty list)
bool("False")  # True  (non-empty string)
```

### Short-Circuit Evaluation

`and` / `or` stop as soon as the result is known, and they **return one of the operands**, not necessarily a `bool`.

- `a and b` -> returns `a` if `a` is falsy, otherwise `b`.
- `a or b` -> returns `a` if `a` is truthy, otherwise `b`.

```python
0 and 5          # 0
3 and 5          # 5
0 or 5           # 5
3 or 5           # 3
"" or "default"  # "default"
not 0            # True  (`not` always returns bool)
```

**Common use — safe access and default values:**

```python
user and user.name          # avoids AttributeError if user is None
name = input_name or "Guest"

if x != 0 and 10 / x > 2:   # second part not evaluated when x == 0
    ...
```

---

## Assignment Operators

|**Operator**|**Equivalent to**|**Example (x = 10)**|**Result**|
|---|---|---|---|
|`=`|—|`x = 10`|`10`|
|`+=`|`x = x + n`|`x += 3`|`13`|
|`-=`|`x = x - n`|`x -= 3`|`7`|
|`*=`|`x = x * n`|`x *= 3`|`30`|
|`/=`|`x = x / n`|`x /= 4`|`2.5`|
|`//=`|`x = x // n`|`x //= 3`|`3`|
|`%=`|`x = x % n`|`x %= 3`|`1`|
|`**=`|`x = x ** n`|`x **= 2`|`100`|
|`&=` `\|=` `^=`|bitwise versions|`x &= 6`|—|
|`<<=` `>>=`|shift versions|`x <<= 1`|`20`|

**Mutable vs. immutable behavior:**

```python
a = [1, 2]
b = a
a += [3]         # in-place: modifies the same list
print(b)         # [1, 2, 3]

a = [1, 2]
b = a
a = a + [3]      # creates a NEW list
print(b)         # [1, 2]

n = 5
n += 1           # ints are immutable: n now points to a new object
```

### The Walrus Operator `:=` (Python 3.8+)

**Assignment expression**: assigns a value and returns it within a larger expression.

```python
if (n := len(items)) > 10:
    print(f"Too many: {n}")

while (line := input("> ")) != "quit":
    print(line)

squares = [y for x in data if (y := x * x) > 10]
```

- Parentheses are usually required.
- Use sparingly; readability comes first.

---

## Bitwise Operators

Operate on the **binary representation** of integers.

|**Operator**|**Name**|**Example** (`a=6` `0110`, `b=3` `0011`)|**Result**|
|---|---|---|---|
|`&`|AND|`a & b`|`2` (`0010`)|
|`\|`|OR|`a \| b`|`7` (`0111`)|
|`^`|XOR|`a ^ b`|`5` (`0101`)|
|`~`|NOT (invert)|`~a`|`-7`|
|`<<`|Left shift|`a << 1`|`12`|
|`>>`|Right shift|`a >> 1`|`3`|

**Key points:**

- `~x` equals `-(x + 1)` (two's complement).
- `x << n` is `x * 2**n`; `x >> n` is `x // 2**n`.
- Python integers have arbitrary size, so there is no overflow.

```python
bin(10)          # '0b1010'
int("1010", 2)   # 10
0b1010           # binary literal
0xFF             # hex literal -> 255
0o17             # octal literal -> 15
```

**Typical uses — flags and tricks:**

```python
x & 1 == 0          # check if even  (careful: use (x & 1) == 0)
x & (1 << k)        # test bit k
x | (1 << k)        # set bit k
x & ~(1 << k)       # clear bit k
x ^ (1 << k)        # toggle bit k
a ^= b; b ^= a; a ^= b   # XOR swap (use a, b = b, a instead)
```

---

## Identity Operators

|**Operator**|**Meaning**|
|---|---|
|`is`|Both names refer to the **same object**|
|`is not`|They refer to **different objects**|

```python
a = [1, 2]
b = a
c = [1, 2]

a is b       # True   (same object)
a is c       # False  (different objects)
a == c       # True   (equal values)
```

- `is` compares `id()`, `==` compares values.
- **Always use `is` for `None`, `True`, `False`:** `if x is None`.
- Do **not** use `is` for numbers or strings: small-int and string caching is an implementation detail.

```python
a = 256; b = 256
a is b        # True  (cached in CPython)
a = 1000; b = 1000
a is b        # may be False
```

---

## Membership Operators

|**Operator**|**Meaning**|
|---|---|
|`in`|Value is found in the container|
|`not in`|Value is **not** found|

```python
3 in [1, 2, 3]           # True
"a" in "banana"          # True (substring check)
"ban" in "banana"        # True
"x" not in "banana"      # True
"key" in {"key": 1}      # True (checks KEYS)
1 in {"key": 1}          # False (not a key)
(1, 2) in [(1, 2), (3,)] # True
```

**Performance:**

|**Container**|**`in` complexity**|
|---|---|
|`list`, `tuple`|O(n)|
|`set`, `dict`|O(1) average|
|`str` (substring)|O(n·m) worst case|

Use a `set` for fast repeated membership checks.

---

## Operator Precedence and Associativity

**Precedence** decides which operator is evaluated first; **associativity** decides the order among operators of the same precedence.

**From highest to lowest priority:**

|**Level**|**Operators**|**Associativity**|
|---|---|---|
|1|`( )` parentheses, `[ ]`, `{ }`, calls `f()`, attribute `x.y`|—|
|2|`**`|right|
|3|`+x`, `-x`, `~x` (unary)|right|
|4|`*`, `/`, `//`, `%`, `@`|left|
|5|`+`, `-`|left|
|6|`<<`, `>>`|left|
|7|`&`|left|
|8|`^`|left|
|9|`\|`|left|
|10|`==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `is not`, `in`, `not in`|chained|
|11|`not`|right|
|12|`and`|left|
|13|`or`|left|
|14|`if ... else` (ternary)|right|
|15|`lambda`|—|
|16|`:=`|—|

```python
2 + 3 * 4          # 14  (* before +)
(2 + 3) * 4        # 20
2 ** 3 ** 2        # 512 (right-assoc)
-3 ** 2            # -9
not a == b         # not (a == b)
a or b and c       # a or (b and c)
10 - 5 - 2         # 3   (left-assoc: (10 - 5) - 2)
```

**Tip:** when in doubt, add parentheses; they cost nothing and improve readability.

---

## Conditional Expression (Ternary Operator)

```python
value = a if condition else b
```

- Evaluates `condition` first; then only one of `a` / `b`.
- It is an **expression**, so it can be used inside other expressions.

```python
status = "adult" if age >= 18 else "minor"
abs_x = x if x >= 0 else -x
print("even" if n % 2 == 0 else "odd")

# Nested (avoid deep nesting)
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
```

---

## Other Operators

### Matrix Multiplication `@`

```python
# used mainly with NumPy arrays
A @ B
```

### Unpacking Operators `*` and `**`

```python
a = [1, 2]
b = [3, 4]
[*a, *b]                 # [1, 2, 3, 4]

d1 = {"x": 1}
d2 = {"y": 2}
{**d1, **d2}             # {'x': 1, 'y': 2}

print(*a)                # print(1, 2)
```

### Dictionary Merge `|` (Python 3.9+)

```python
{"a": 1} | {"b": 2}      # {'a': 1, 'b': 2}
d1 |= d2                 # in-place update
```

### Slicing, Indexing, Call

```python
s[0]          # indexing
s[1:4]        # slicing
s[::-1]       # reversed
f(x)          # call
obj.attr      # attribute access
```

---

## Type Conversion in Expressions

**Implicit (numeric promotion):** `int` -> `float` -> `complex`.

```python
1 + 2.5        # 3.5 (float)
True + 1       # 2   (bool is a subclass of int)
```

**Explicit conversion:**

```python
int("42")        # 42
int(3.9)         # 3  (truncates toward zero)
float("3.14")    # 3.14
str(10)          # "10"
bool("")         # False
round(3.5)       # 4
round(2.5)       # 2  (banker's rounding: ties to even)
```

- There is **no** implicit conversion between `str` and numbers: `"5" + 5` -> `TypeError`.

---

## Operator Overloading (Brief)

Operators are mapped to **special (dunder) methods**, so custom classes can define their own behavior.

|**Operator**|**Method**|
|---|---|
|`+`|`__add__`|
|`-`|`__sub__`|
|`*`|`__mul__`|
|`/`|`__truediv__`|
|`==`|`__eq__`|
|`<`|`__lt__`|
|`len(x)`|`__len__`|
|`x[i]`|`__getitem__`|
|`in`|`__contains__`|

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v = Vector(1, 2) + Vector(3, 4)   # calls __add__
```

---

## Common Pitfalls

|**Mistake**|**Problem / Fix**|
|---|---|
|`if x = 5:`|`SyntaxError`; use `==` for comparison|
|`0.1 + 0.2 == 0.3`|Float error; use `math.isclose()`|
|`x is 1000`|Unreliable; use `==`|
|`if x == None:`|Works, but use `if x is None:`|
|`a == b or c`|Means `(a == b) or c`; write `a == b or a == c` or `a in (b, c)`|
|`7 / 2` expecting `3`|`/` is true division; use `//`|
|`-7 // 2` expecting `-3`|Floor division gives `-4`|
|`"5" + 5`|`TypeError`; convert explicitly|
|`a += [x]` vs `a = a + [x]`|In-place vs new object; affects aliases|
|`not x == y`|Parsed as `not (x == y)`; prefer `x != y`|

---

## Summary

- An **expression** produces a value; a **statement** performs an action.
- **Arithmetic:** `+ - * / // % **`; `/` always returns `float`, `//` floors, `%` follows the divisor's sign.
- **Comparison:** `== != < > <= >=`; supports **chaining** (`1 < x < 10`).
- **Logical:** `and`, `or`, `not`; short-circuit and return an **operand**, not necessarily a `bool`.
- **Assignment:** `=`, augmented (`+=`, ...), and walrus `:=`.
- **Bitwise:** `& | ^ ~ << >>` work on integer bits.
- **Identity:** `is` / `is not` compare objects; **membership:** `in` / `not in` search containers.
- **Precedence:** `**` > unary > `* / // %` > `+ -` > shifts > bitwise > comparisons > `not` > `and` > `or` > ternary; use parentheses when unsure.
- **Ternary:** `a if cond else b`.
- Operators map to dunder methods, enabling **operator overloading**.