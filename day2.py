"""
Day 2 Practice — File I/O, Exceptions, OOP Basics
Data Engineer 30-Day Prep

Push this file to: data-engineer-portfolio/day02/practice.py
"""

# ----------------------------------------------------------------------
# Problem 1: Write a list of dicts to a CSV file, then read it back
# ----------------------------------------------------------------------
import csv

def write_users_csv(users, path="users.csv"):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "age"])
        writer.writeheader()
        writer.writerows(users)

def read_users_csv(path="users.csv"):
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

users = [
    {"id": 1, "name": "Ravi", "age": 25},
    {"id": 2, "name": "Sana", "age": 30},
]
write_users_csv(users)
print(read_users_csv())
# Output: [{'id': '1', 'name': 'Ravi', 'age': '25'}, {'id': '2', 'name': 'Sana', 'age': '30'}]


# ----------------------------------------------------------------------
# Problem 2: Read a JSON file and handle the case where it doesn't exist
# ----------------------------------------------------------------------
import json

def safe_load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {path}. Returning empty dict.")
        return {}

print(safe_load_json("does_not_exist.json"))
# Output: File not found: does_not_exist.json. Returning empty dict.
#         {}


# ----------------------------------------------------------------------
# Problem 3: Write a function that safely converts a list of strings
# to integers, skipping (and logging) invalid ones
# ----------------------------------------------------------------------
def safe_convert_to_int(values):
    result = []
    for v in values:
        try:
            result.append(int(v))
        except ValueError:
            print(f"Skipping invalid value: {v}")
    return result

print(safe_convert_to_int(["1", "2", "abc", "4"]))
# Output: Skipping invalid value: abc
#         [1, 2, 4]


# ----------------------------------------------------------------------
# Problem 4: Custom exception — raise an error if a "config" dict
# is missing a required key
# ----------------------------------------------------------------------
class MissingConfigError(Exception):
    pass

def validate_config(config, required_keys):
    for key in required_keys:
        if key not in config:
            raise MissingConfigError(f"Missing required config key: '{key}'")
    return True

try:
    validate_config({"source": "s3"}, ["source", "destination"])
except MissingConfigError as e:
    print(e)
# Output: Missing required config key: 'destination'


# ----------------------------------------------------------------------
# Problem 5: Build a simple class hierarchy — BaseLoader + CSVLoader
# ----------------------------------------------------------------------
class BaseLoader:
    def __init__(self, source_path):
        self.source_path = source_path

    def load(self):
        raise NotImplementedError("Subclasses must implement load()")

    def __repr__(self):
        return f"{self.__class__.__name__}(source_path='{self.source_path}')"


class CSVLoader(BaseLoader):
    def load(self):
        return read_users_csv(self.source_path)


loader = CSVLoader("users.csv")
print(loader)          # CSVLoader(source_path='users.csv')
print(loader.load())   # loads the CSV we wrote in Problem 1


# ----------------------------------------------------------------------
# Problem 6: Use try/except/else/finally together in one function
# ----------------------------------------------------------------------
def process_record(record):
    try:
        age = int(record["age"])
    except (KeyError, ValueError) as e:
        print(f"Failed to process record: {e}")
        return None
    else:
        print(f"Successfully processed age: {age}")
        return age
    finally:
        print("Finished attempting to process record.\n")

process_record({"age": "25"})
process_record({"age": "not_a_number"})
process_record({})
