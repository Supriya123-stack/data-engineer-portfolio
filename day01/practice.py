"""
Day 1 Practice — Python Core Fundamentals
Data Engineer 30-Day Prep

Each problem includes the question as a comment, followed by the solution.
Push this file to: data-engineer-30-day-prep/day01/practice.py
"""

# ----------------------------------------------------------------------
# Problem 1: Return only the even numbers from a list using a comprehension
# ----------------------------------------------------------------------
def get_evens(numbers):
    return [n for n in numbers if n % 2 == 0]

print(get_evens([1, 2, 3, 4, 5, 6]))
# Output: [2, 4, 6]


# ----------------------------------------------------------------------
# Problem 2: From a list of dicts, return names of people who scored above 75
# ----------------------------------------------------------------------
def high_scorers(data, threshold=75):
    return [person["name"] for person in data if person["score"] > threshold]

data = [
    {"name": "A", "score": 90},
    {"name": "B", "score": 60},
    {"name": "C", "score": 85},
]
print(high_scorers(data))
# Output: ['A', 'C']


# ----------------------------------------------------------------------
# Problem 3: Clean a string — strip whitespace, lowercase, remove punctuation
# ----------------------------------------------------------------------
import string

def clean_string(s):
    s = s.strip().lower()
    return s.translate(str.maketrans("", "", string.punctuation))

print(clean_string("  Hello, World!!  "))
# Output: 'hello world'


# ----------------------------------------------------------------------
# Problem 4: Simulate a simple ETL step — fill missing "age" key with None
# ----------------------------------------------------------------------
def clean_records(records):
    cleaned = []
    for record in records:
        record = record.copy()
        if "age" not in record:
            record["age"] = None
        cleaned.append(record)
    return cleaned

raw = [{"name": "Ravi", "age": 25}, {"name": "Sana"}]
print(clean_records(raw))
# Output: [{'name': 'Ravi', 'age': 25}, {'name': 'Sana', 'age': None}]


# ----------------------------------------------------------------------
# Problem 5: Combine unique elements from any number of lists using *args
# ----------------------------------------------------------------------
def combine_unique(*lists):
    result = set()
    for lst in lists:
        result.update(lst)
    return result

print(combine_unique([1, 2, 3], [3, 4, 5], [5, 6]))
# Output: {1, 2, 3, 4, 5, 6}


# ----------------------------------------------------------------------
# Problem 6: Predict the output
# ----------------------------------------------------------------------
nums = [1, 2, 3, 4, 5, 6]
result = [n for n in nums if n % 2 == 0]
print(result)
# Output: [2, 4, 6]


# ----------------------------------------------------------------------
# Problem 7: One-line dict comprehension mapping each string to its length
# ----------------------------------------------------------------------
lengths = {word: len(word) for word in ["a", "bb", "ccc"]}
print(lengths)
# Output: {'a': 1, 'bb': 2, 'ccc': 3}


# ----------------------------------------------------------------------
# Problem 8: Fix the mutable default argument bug
# ----------------------------------------------------------------------
# BUGGY VERSION (don't use — the default list is shared across calls):
#
# def add_item(item, my_list=[]):
#     my_list.append(item)
#     return my_list

# FIXED VERSION:
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item("x"))  # ['x']
print(add_item("y"))  # ['y']  <- correct, doesn't remember previous call


# ----------------------------------------------------------------------
# Problem 9: Count unique words in a sentence (case-insensitive) using a set
# ----------------------------------------------------------------------
def unique_words(text):
    words = text.lower().split()
    return len(set(words))

print(unique_words("Data is data and data is powerful"))
# Output: 4  ('data', 'is', 'and', 'powerful')


# ----------------------------------------------------------------------
# Problem 10: List comprehension version of Problem 2 (names scoring >= 75)
# ----------------------------------------------------------------------
names_75_plus = [p["name"] for p in data if p["score"] >= 75]
print(names_75_plus)
# Output: ['A', 'C']
