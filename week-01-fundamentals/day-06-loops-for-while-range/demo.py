# demo.py — simple demo of loops: for, while, range

# for over different types
print("for:")
for fruit in ["apple", "banana", "cherry"]:
    print(" ", fruit)

print("  chars:", end=" ")
for ch in "Python":
    print(ch, end=" ")
print()

# dict iteration
d = {"a": 1, "b": 2}
print("\ndict:")
for key in d:
    print("  key:", key)
for key, value in d.items():
    print(f"  {key} -> {value}")

# enumerate and zip
names = ["Ali", "Bek", "Cat"]
ages = [20, 21, 22]
print("\nenumerate / zip:")
for i, name in enumerate(names, start=1):
    print(f"  {i}. {name}")
for name, age in zip(names, ages):
    print(f"  {name} is {age}")

# reversed
print("  reversed:", list(reversed([1, 2, 3])))

# range
print("\nrange:")
print("  range(5)          ->", list(range(5)))
print("  range(2, 6)       ->", list(range(2, 6)))
print("  range(0, 10, 3)   ->", list(range(0, 10, 3)))
print("  range(10, 0, -2)  ->", list(range(10, 0, -2)))
print("  range(5, 2)       ->", list(range(5, 2)), "(empty)")
r = range(10)
print(f"  len={len(r)}, r[3]={r[3]}, r[-1]={r[-1]}, 5 in r -> {5 in r}")
print("  sum(range(1, 101)) =", sum(range(1, 101)))

# repeat N times
print("\nrepeat:")
for _ in range(3):
    print("  Hello")

# while
print("\nwhile:")
count = 1
while count <= 5:
    print("  count:", count)
    count += 1

# while with a collection
stack = [1, 2, 3]
print("  pop:", end=" ")
while stack:
    print(stack.pop(), end=" ")
print()

# while True + break
n = 0
while True:
    n += 1
    if n == 3:
        break
print("  while True + break stopped at", n)

# break / continue
print("\nbreak / continue:")
print("  break at 5:   ", [i for i in range(10) if i < 5])
for i in range(6):
    if i % 2 == 0:
        continue
    print("  odd:", i)

# else on a loop
print("\nloop else:")
for n in range(2, 10):
    if n == 7:
        print("  Found 7")
        break
else:
    print("  Not found")

for n in range(2, 5):
    if n == 7:
        break
else:
    print("  No break -> else runs")


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            break
    else:
        return True
    return False


print("  primes up to 30:", [n for n in range(31) if is_prime(n)])

# nested loops
print("\nmultiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

print("\npattern:")
for i in range(1, 5):
    print("*" * i)

# break out of two loops via function
matrix = [[1, 2], [3, 4], [5, 6]]


def find(matrix, target):
    for row in matrix:
        for x in row:
            if x == target:
                return True
    return False


print("\nfind 4:", find(matrix, 4), "| find 9:", find(matrix, 9))

# modifying a list while iterating
nums = [1, 2, 3, 4, 5, 6]
print("\nremove evens safely:", [n for n in nums if n % 2 != 0])

# comprehensions
print("\ncomprehensions:")
print("  squares:", [x ** 2 for x in range(5)])
print("  evens:  ", [x for x in range(10) if x % 2 == 0])
print("  dict:   ", {x: x ** 2 for x in range(3)})

# common patterns
total = 0
for x in [3, 5, 7]:
    total += x
print("\nsum:", total)

nums = [4, 9, 2, 7]
biggest = nums[0]
for n in nums[1:]:
    if n > biggest:
        biggest = n
print("max:", biggest)

# factorial and Fibonacci
result = 1
for i in range(2, 6):
    result *= i
print("5! =", result)

a, b = 0, 1
print("fibonacci:", end=" ")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()

# retry with limit (simulated)
passwords = ["x", "y", "secret"]
attempts = 0
while attempts < 3:
    password = passwords[attempts]
    if password == "secret":
        print("retry: Access granted on attempt", attempts + 1)
        break
    attempts += 1
else:
    print("retry: Too many attempts")
