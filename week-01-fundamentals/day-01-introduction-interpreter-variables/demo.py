# 1. Variable creation
x = 10
print("Value:", x)
print("Type:", type(x))

# 2. Dynamic typing
x = "Hello Python"
print("\nNew value:", x)
print("New type:", type(x))

# 3. Multiple variables referencing
a = [1, 2, 3]
b = a

b.append(4)

print("\na:", b)
print("b:", b)
print("Same object:", a is b)

# 4. Input and Output
name = input("\nEnter your name: ")
print(f"Hello, {name}")

# 5.Program completion
print("\nProgram finished!")
