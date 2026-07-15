# Day 3 Notes — Lambda Functions & map()
*(Based on my own practice file)*

## 1. Lambda Functions

A lambda is a small anonymous function used for short, one-line operations.

**Syntax**
```python
var_name = lambda args: expression
print(var_name(values))
```

**Example — square and cube of a number**
```python
a = lambda c: [c**2, c**3]
print(a(2))
# Output: [4, 8]
```

**Syntax with if-else inside lambda**
```python
var_name = lambda args: TRUE_RESULT if condition else FALSE_RESULT
```

**Example — check if a number is odd or even**
```python
a = lambda x: "EVEN" if x % 2 == 0 else "ODD"
print(a(67))
# Output: ODD
```

---

## 2. map() Function

`map()` is a built-in function that applies another function to every item in a collection (list, set, tuple, dict).

**Syntax**
```python
var_name = map(function_name, collection)
print(var_name)   # returns a map object — must convert to list/tuple to see values
```

**Example — square each number in a list**
```python
sqr = lambda a: a**2
sqr_var = map(sqr, [1, 2, 3, 4])
print(list(sqr_var))
# Output: [1, 4, 9, 16]
```

Can also be written directly with lambda inline:
```python
print(list(map(lambda a: a**2, [1, 2, 3, 4])))
# Output: [1, 4, 9, 16]
```

---

## 3. Practical Examples From My Practice File

**Factorial of every number in a tuple**
```python
def fact(n):
    if n < 1 or n == 0:
        return 1
    return n * fact(n - 1)

print(tuple(map(fact, [1, 2, 3, 4, 5])))
# Output: (1, 2, 6, 24, 120)
```

**Square each element without map() — plain loop version**
```python
c = eval(input("enter the collection:"))
b = []
for i in c:
    b.append(i**2)
print(b)
```

**Square only even numbers using map()**
```python
def sqr(a):
    if a % 2 == 0:
        return a**2

ab = map(sqr, [1, 2, 3, 4, 5, 6])
print(list(ab))
# Output: [None, 4, None, 16, None, 36]
# Note: odd numbers return None since the function has no explicit return for them
```

**Cube of numbers in a range, as a dictionary**
```python
start = int(input("enter the starting value:"))
end = int(input("enter the ending value:"))
x = range(start, end)
print(dict(map(lambda a: (a, a**2), x)))
# (Note: this squares, not cubes — matches what the code actually does)
```

**Reverse each word in a sentence, as a dictionary**
```python
s = "program on map function".split()
print(dict(map(lambda i: (i, i[::-1]), s)))
# Output: {'program': 'margorp', 'on': 'no', 'map': 'pam', 'function': 'noitcnuf'}
```

---

## Key Takeaways
- `lambda` is for short, throwaway functions — not meant for complex logic.
- `map()` always returns a **map object**, not a list — must wrap in `list()`, `tuple()`, or `dict()` to see/use the actual results.
- A function passed into `map()` that doesn't return anything for some inputs (like the "square only even numbers" example) will silently produce `None` for the skipped items — worth double-checking output carefully.
- `map()` can take **more than one collection** at once, applying the function pairwise across them.
- This pattern (`map()` + `lambda`) is the foundation for `.apply()` in Pandas later — same idea, applied to DataFrame columns instead of plain lists.

## One Thing to Double-Check in My Own Code
The "cube of numbers" example is labeled as cube but the lambda actually computes `a**2` (square), not `a**3` (cube). Worth fixing before committing — recruiters do read code closely.
