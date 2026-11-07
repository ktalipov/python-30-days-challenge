# demo_strings.py — simple demo of strings and string methods

# Indexing and slicing
s = "Python"
print("Indexing / slicing:")
print(f"  s[0]     = {s[0]!r}")
print(f"  s[-1]    = {s[-1]!r}")
print(f"  s[0:2]   = {s[0:2]!r}")
print(f"  s[::2]   = {s[::2]!r}")
print(f"  s[::-1]  = {s[::-1]!r}")

# Immutability
print("\nImmutability:")
try:
    s[0] = "X"
except TypeError as e:
    print(f"  s[0] = 'X' -> TypeError: {e}")
print(f"  new string: {'X' + s[1:]!r}")

# Case
text = "hello world"
print("\nCase:")
print(f"  upper()      -> {text.upper()!r}")
print(f"  title()      -> {text.title()!r}")
print(f"  capitalize() -> {text.capitalize()!r}")
print(f"  'Straße'.casefold() -> {'Straße'.casefold()!r}")

# Searching
print("\nSearching:")
print(f"  find('o')   -> {text.find('o')}")
print(f"  rfind('o')  -> {text.rfind('o')}")
print(f"  find('z')   -> {text.find('z')}")
print(f"  count('l')  -> {text.count('l')}")
print(f"  startswith('hell') -> {text.startswith('hell')}")
print(f"  'photo.png'.endswith(('.png', '.jpg')) -> {'photo.png'.endswith(('.png', '.jpg'))}")

# Checks
print("\nChecks:")
print(f"  'abc'.isalpha()  -> {'abc'.isalpha()}")
print(f"  '123'.isdigit()  -> {'123'.isdigit()}")
print(f"  '-5'.isdigit()   -> {'-5'.isdigit()}")
print(f"  ''.isalpha()     -> {''.isalpha()}")

# Trimming
print("\nTrimming:")
print(f"  '  hi  '.strip() -> {'  hi  '.strip()!r}")
print(f"  'text.txt'.rstrip('.txt')       -> {'text.txt'.rstrip('.txt')!r}  (pitfall!)")
print(f"  'text.txt'.removesuffix('.txt') -> {'text.txt'.removesuffix('.txt')!r}")

# Split / join
print("\nSplit / join:")
print(f"  'a,b,c'.split(',')      -> {'a,b,c'.split(',')}")
print(f"  'a  b   c'.split()      -> {'a  b   c'.split()}")
print(f"  'k=v=x'.partition('=')  -> {'k=v=x'.partition('=')}")
print(f"  ', '.join(['a','b','c']) -> {', '.join(['a', 'b', 'c'])!r}")
print(f"  ', '.join(map(str,[1,2])) -> {', '.join(map(str, [1, 2]))!r}")

# Replace / translate
print("\nReplace / translate:")
print(f"  replace('l','L')    -> {text.replace('l', 'L')!r}")
table = str.maketrans("", "", "aeiou")
print(f"  remove vowels       -> {'education'.translate(table)!r}")

# Padding
print("\nPadding:")
print(f"  center(8,'*') -> {'ab'.center(8, '*')!r}")
print(f"  ljust(5,'.')  -> {'ab'.ljust(5, '.')!r}")
print(f"  rjust(5,'.')  -> {'ab'.rjust(5, '.')!r}")
print(f"  zfill(5)      -> {'-42'.zfill(5)!r}")

# f-string formatting
name, age, price = "Ali", 20, 1234.5
print("\nFormatting:")
print(f"  {name} is {age} years old")
print(f"  {age=}")
print(f"  price: {price:>12,.2f}")
print(f"  percent: {0.256:.1%}")
print(f"  binary: {10:b}, hex: {255:x}, padded: {42:05d}")

# Raw strings and escapes
print("\nEscapes / raw:")
print("  Col1\tCol2")
print(f"  normal: {'C:\\new'}")
print(rf"  raw:    C:\new\table")

# bytes <-> str
word = "Привет"
b = word.encode("utf-8")
print("\nEncoding:")
print(f"  {word!r} -> {b}")
print(f"  back: {b.decode('utf-8')!r}")
print(f"  len(str)={len(word)}, len(bytes)={len(b)}")

# Unicode normalization
import unicodedata
a = "é"
c = "e\u0301"
print("\nUnicode:")
print(f"  a == c: {a == c}, len: {len(a)} vs {len(c)}")
print(f"  after NFC: {unicodedata.normalize('NFC', c) == a}")

# Fast concatenation
words = ["fast", "string", "building"]
print(f"\njoin: {' '.join(words)!r}")
