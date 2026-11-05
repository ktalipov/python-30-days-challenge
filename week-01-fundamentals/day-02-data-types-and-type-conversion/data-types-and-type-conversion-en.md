# Data Types and Type Conversion in Python

## Data Types

A data type in Python is an attribute of an object that determines what values it can store and what operations can be performed on it. The type belongs to the object, not the variable, and is determined at runtime (`type(x)`).

Main built-in types: `int`, `float`, `bool`, `str`, `list`, `tuple`, `dict`, `set`, `NoneType`.

### Main built-in Python data types:

|**Category**|**Types**|**Examples**|
|---|---|---|
|**Numeric**|`int`, `float`, `complex`|`10`, `3.14`, `2+3j`|
|**Boolean**|`bool`|`True`, `False`|
|**String**|`str`|`"text"`|
|**Sequences**|`list`, `tuple`, `range`|`[1, 2]`, `(1, 2)`, `range(5)`|
|**Mappings**|`dict`|`{"a": 1}`|
|**Sets**|`set`, `frozenset`|`{1, 2, 3}`|
|**Binary**|`bytes`, `bytearray`, `memoryview`|`b"abc"`|
|**No value**|`NoneType`|`None`|

### Classification by Mutability:

- **Immutable:** `int`, `float`, `complex`, `bool`, `str`, `tuple`, `frozenset`, `bytes`, `None`
    
- **Mutable:** `list`, `dict`, `set`, `bytearray`
    

### Classification by Structure:

- **Scalar (simple):** `int`, `float`, `bool`, `complex`, `None`
    
- **Collections (composite):** `str`, `list`, `tuple`, `dict`, `set`, `range`
    

**Type checking:** `type(x)` or `isinstance(x, int)`

---

## Type Conversion

**Type conversion** (type casting) is changing a value of one data type into another. Conversion creates a **new object**; the original object is not modified.

### 1. Implicit conversion

Python converts types automatically when it is safe and there is no loss of information (usually to the "wider" type).

```python
1 + 2.5      # 3.5   (int -> float)
True + 1     # 2     (bool -> int)
2 + 3j       # (2+3j) (int -> complex)
```

Python is strongly typed, so it does **not** implicitly convert incompatible types:

```python
"5" + 5      # TypeError
```

### 2. Explicit conversion

The programmer calls a type's constructor function.

|**Function**|**Converts to**|**Example**|**Result**|
|---|---|---|---|
|`int()`|integer|`int("42")`, `int(3.9)`|`42`, `3`|
|`float()`|floating-point|`float("3.14")`, `float(5)`|`3.14`, `5.0`|
|`str()`|string|`str(10)`, `str([1, 2])`|`"10"`, `"[1, 2]"`|
|`bool()`|boolean|`bool(0)`, `bool("a")`|`False`, `True`|
|`list()`|list|`list("abc")`, `list((1, 2))`|`['a', 'b', 'c']`, `[1, 2]`|
|`tuple()`|tuple|`tuple([1, 2])`|`(1, 2)`|
|`set()`|set|`set([1, 1, 2])`|`{1, 2}`|
|`dict()`|dictionary|`dict([("a", 1)])`|`{'a': 1}`|

### Important details

- `int(3.9)` **truncates** toward zero (gives `3`), it does not round. Use `round()` for rounding.
- `int("3.5")` raises `ValueError`; convert via float: `int(float("3.5"))`.
- `set()` removes duplicates and does not keep the original order.
- `str(x)` works for any object; `int()` and `float()` work only for valid numeric values.

### 3. Conversion errors

If the value cannot be converted, an exception is raised:

```python
int("abc")    # ValueError
int(None)     # TypeError
```

Handle it with `try/except`:

```python
try:
    n = int(input("Number: "))
except ValueError:
    print("Not a number")
```

### 4. Boolean conversion (truthy and falsy)

`bool(x)` returns `False` for these values, and `True` for everything else:

- `0`, `0.0`, `0j`
- `""` (empty string)
- `[]`, `()`, `{}`, `set()`, `range(0)`
- `None`
- `False`

```python
bool(0)        # False
bool("")       # False
bool([])       # False
bool("0")      # True  (non-empty string)
bool([0])      # True  (non-empty list)
```

### 5. Typical use case

`input()` always returns a `str`, so numbers must be converted:

```python
age = int(input("Age: "))
price = float(input("Price: "))
```

---

## Summary

- Type conversion creates a new object of another type.
- **Implicit:** done automatically for compatible numeric types (`int` -> `float`).
- **Explicit:** done with `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, `dict()`.
- Incompatible values raise `ValueError` or `TypeError`.
- Falsy values: `0`, `""`, `[]`, `()`, `{}`, `set()`, `None`; everything else is truthy.