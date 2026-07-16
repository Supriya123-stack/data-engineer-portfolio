# Day 4 Notes — filter() & reduce()
*(Based on my own practice file)*

## 1. filter() Function

`filter()` is a built-in function used to extract only the required values from a collection — it keeps items where the given function returns `True`, and discards the rest.

**Syntax**
```python
var_name = filter(function_name, collection)
print(list(var_name))   # filter returns a filter object — convert to list/tuple to see values
```

**Example — extract only even numbers from a range**
```python
print(list(filter(lambda a: a % 2 == 0, range(2, 6))))
# Output: [2, 4]
```

**Example — extract only string items from a tuple**
```python
x = (2, 'supriya', 5+2j, 's', True)
print(tuple(filter(lambda a: type(a) == str, x)))
# Output: ('supriya', 's')
```

**Example — extract strings that start lowercase and end uppercase**
```python
data = ('supriyA', 33, 4+4j, 'S', 'pramodA')
result = filter(lambda x: isinstance(x, str) and x[0].islower() and x[-1].isupper(), data)
print(tuple(result))
# Output: ('supriyA', 'pramodA')
```
Note: `'S'` is excluded because it's only one character — `x[0]` and `x[-1]` are the same character, and a single uppercase letter can't satisfy "starts lowercase."

---

## 2. Combining filter() + map()

A very common real pattern: use `filter()` to select the items you want, then `map()` to transform them.

**Example — square all even integers in a mixed list**
```python
a = [10, 20, 'hello', 5+6j, 85, 90, 37, 90.00]
result = map(lambda x: x**2, filter(lambda y: type(y) == int and y % 2 == 0, a))
print(list(result))
# Output: [100, 400, 8100]
```
Here `filter()` first keeps only integers that are even (`10, 20, 90`), then `map()` squares each of them.

**Example — extract collection-type items with even length**
```python
data = [[10, 20], 30+5j, 'hello', (1, 2, 3), 'True', True]
result = filter(lambda x: type(x) in (int, str, list, tuple) and len(x) % 2 == 0, data)
print(list(result))
# Output: [[10, 20], 'True']
```
Note: `len()` only works on things that have a length (str, list, tuple, etc.) — that's why the condition checks `type(x) in (...)` first, to avoid calling `len()` on something like a complex number, which would raise an error.

---

## 3. reduce() Function

`reduce()` is used to perform a running operation *between* elements of a collection, reducing it down to a single final value. Unlike `map()`/`filter()`, it's not built in by default — it must be imported from `functools`.

**Syntax**
```python
from functools import reduce
var_name = reduce(func_name, collection)
print(var_name)
```

**Example — sum all numbers in a list**
```python
from functools import reduce

add = lambda s, i: s + i
out = reduce(add, [1, 2, 3, 4, 5, 6])
print(out)
# Output: 21
```
How it works step by step: `((((((1+2)+3)+4)+5)+6)`  — each step carries forward the running total (`s`) and combines it with the next item (`i`).

**Example — find the maximum number in a collection**
```python
print(reduce(lambda a, b: a if a > b else b, [10, 30, 40, 70]))
# Output: 70
```
Same idea — at each step, keep whichever of the two values is bigger, carry it forward, compare with the next item.

---

## Key Takeaways
- `filter()` keeps items, `map()` transforms items, `reduce()` collapses everything into one final value — these three together cover most "process a collection" needs without writing manual loops.
- Both `filter()` and `map()` return lazy objects (`filter object`, `map object`) — nothing is actually computed until you convert to `list()`/`tuple()` or iterate over it.
- `reduce()` needs an explicit import (`from functools import reduce`) — it's not a built-in like `map()`/`filter()`.
- Chaining `filter()` inside `map()` (or vice versa) is a common, useful pattern — filter first to narrow down what you're working with, then transform what's left.
- When checking types before calling something like `len()`, always validate the type first (as done with `type(x) in (...)`) — calling a method on the wrong type raises an error and can crash a pipeline.

## Where This Applies in Real Data Engineering Work
This same filter → transform → aggregate pattern is exactly what you'll do constantly with Pandas (`.filter()`, `.apply()`, `.groupby().agg()`) and PySpark (`.filter()`, `.map()`, `.reduce()` at scale). Understanding it here with plain Python makes those tools much easier to pick up later — they're the same logic, just applied to bigger, structured data.
