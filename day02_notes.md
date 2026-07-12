# Day 2 Notes — File I/O, Exceptions, OOP Basics

## 1. File I/O

**Reading and writing text files**
```python
# Writing
with open("data.txt", "w") as f:
    f.write("Hello, Data Engineer!\n")

# Reading
with open("data.txt", "r") as f:
    content = f.read()
```
`with` automatically closes the file when done — always use it instead of manual `open()`/`close()`.

**Working with CSV**
```python
import csv

# Writing
with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "age"])
    writer.writerow([1, "Ravi", 25])

# Reading
with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # {'id': '1', 'name': 'Ravi', 'age': '25'}
```

**Working with JSON**
```python
import json

data = {"name": "Ravi", "age": 25}

# Writing
with open("user.json", "w") as f:
    json.dump(data, f)

# Reading
with open("user.json", "r") as f:
    loaded = json.load(f)
```

**Why this matters for DE work:** almost every pipeline starts with reading raw files (CSV/JSON from an API or S3) and ends with writing transformed output. This is the most-used skill in your daily toolkit.

---

## 2. Exception Handling

```python
try:
    value = int("not_a_number")
except ValueError as e:
    print(f"Conversion failed: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No errors occurred")
finally:
    print("This always runs, error or not")
```

**Raising your own exceptions**
```python
def load_file(path):
    if not path.endswith(".csv"):
        raise ValueError("Only CSV files are supported")
    # ... load logic
```

**Why this matters:** pipelines fail in messy real-world ways — missing files, malformed rows, API timeouts. Good exception handling is what separates a script that silently corrupts data from one that fails loudly and safely. Interviewers care about this a lot for DE roles.

---

## 3. OOP Basics

```python
class DataLoader:
    def __init__(self, source_path, file_format="csv"):
        self.source_path = source_path
        self.file_format = file_format

    def load(self):
        print(f"Loading {self.file_format} file from {self.source_path}")
        # actual loading logic would go here

    def __repr__(self):
        return f"DataLoader(source_path='{self.source_path}')"


loader = DataLoader("data/users.csv")
loader.load()
print(loader)
```

**Inheritance**
```python
class CSVLoader(DataLoader):
    def __init__(self, source_path):
        super().__init__(source_path, file_format="csv")

    def load(self):
        print(f"Loading CSV specifically from {self.source_path}")


class JSONLoader(DataLoader):
    def __init__(self, source_path):
        super().__init__(source_path, file_format="json")

    def load(self):
        print(f"Loading JSON specifically from {self.source_path}")
```

**Why this matters:** pipeline code is rarely one script — it's usually structured as reusable classes (e.g., a base `Loader` class with different subclasses per file type). This is a common pattern in real ETL codebases and shows up in take-home assignments.

---

## Key Takeaways to Remember for Interviews
- Always use `with` for file handling — it's a code-quality signal interviewers notice immediately.
- Know the difference between catching a specific exception (`ValueError`) vs. a broad one (`Exception`) — and why broad catches can hide real bugs.
- Be able to explain why you'd wrap pipeline steps in try/except (fail gracefully, log the error, don't crash the whole job over one bad row).
- Understand basic inheritance — you don't need to be an OOP expert, but you should be able to explain why a `BaseLoader` class with subclasses is cleaner than copy-pasting similar functions.

## Tomorrow (Day 3) Preview
NumPy and Pandas — arrays, Series/DataFrames, and reading/writing CSV/Excel/JSON with Pandas instead of raw Python.
