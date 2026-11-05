# 1. Data types
x = 10
print("Value:", x)
print("Type:", type(x))

x = 3.14
print("\nValue:", x)
print("Type:", type(x))

x = "Hello"
print("\nValue:", x)
print("Type:", type(x))

x = [1, 2, 3]
print("\nValue:", x)
print("Type:", type(x))

# 2. Implicit conversion
result = 1 + 2.5
print("\n1 + 2.5 =", result, type(result))

result = True + 1
print("True + 1 =", result, type(result))

# 3. Explicit conversion
print("\nint('42') =", int("42"))
print("int(3.9) =", int(3.9))
print("float(5) =", float(5))
print("str(10) =", str(10))
print("list('abc') =", list("abc"))
print("set([1, 1, 2]) =", set([1, 1, 2]))

# 4. Conversion error
try:
    int("abc")
except ValueError:
    print("\nCannot convert 'abc' to int")

# 5. Truthy and falsy
print("\nbool(0):", bool(0))
print("bool(''):", bool(""))
print("bool([]):", bool([]))
print("bool('0'):", bool("0"))

# 6. Input and Output
age = int(input("\nEnter your age: "))
print("Next year you will be", age + 1)
print("Type of age:", type(age))

# 7. Program completion
print("\nProgram finished!")
