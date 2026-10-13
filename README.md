# homework

Python course homework, from the basics up to object-oriented programming. Each assignment is in its own folder (`hw1` to `hw14`), and each file solves several small tasks ("ამოცანა" means "task").

> Task descriptions, prompts and comments are in Georgian.

## Requirements

- Python 3.9+ (standard library only)

## Running

```bash
git clone https://github.com/mberd7/homework.git
cd homework
python hw8/homework8.py
```

Most scripts are interactive and ask for input in the terminal. The tasks in a file run one after another.

## Contents

| # | File | Topics | Tasks |
| --- | --- | --- | --- |
| 1 | [`hw1/homework1.py`](hw1/homework1.py) | Input, arithmetic operators | Arithmetic on two numbers, area of a rhombus and a triangle, metre unit conversion, sum of two-digit numbers |
| 2 | [`hw2/homework2.py`](hw2/homework2.py) | Conditionals, `in`, `is` | Membership check in a list, even/odd, identity vs. equality of strings, comparison against list elements |
| 3 | [`hw3/homework3.py`](hw3/homework3.py) | `for` / `while` loops | Sum from 1 to n, countdown, number-guessing game (1–100), sum positive numbers until the user types `sum` |
| 4 | [`hw4/homework4.py`](hw4/homework4.py) | Strings, encoding | UTF-8 encoding, `strip`/`lower`/`replace`, first half of a string, password validation with the `string` module, bytes ⇄ string |
| 5 | [`hw5/homework5.py`](hw5/homework5.py) | Lists, `re` | Interactive list editor (`a` append / `r` remove / `e` exit), list methods (`index`, `pop`, `copy`, `clear`), phone format `(123) 456-789` checked with a regex |
| 6 | [`hw6/homework6.py`](hw6/homework6.py) | Dictionaries | Pick a student by ID and print their info and grades for each subject from a nested dict |
| 7 | [`hw7/homework7.py`](hw7/homework7.py) | Sets, tuples | `set` / `frozenset` from input, union as a tuple, unique elements, tuple unpacking, intersection of two name lists |
| 8 | [`hw8/homework8.py`](hw8/homework8.py) | Functions | Fibonacci sequence, anagram check, factorial, character counting |
| 9 | [`hw9/homework9.py`](hw9/homework9.py) | Scope, recursion | `global` variables, list sum, local vs. global shadowing, recursive digit sum, recursive string reversal |
| 10 | [`hw10/homework10.py`](hw10/homework10.py) | Functional tools, exceptions | `zip` grouping, product using `reduce` and `lambda` with `TypeError` handling, odd filter, `filter` + `endswith` |
| 11 | [`hw11/homework11.py`](hw11/homework11.py) | JSON, context managers | `@contextmanager` path helper, then read, append and update records in a JSON file of chess players |
| 12 | [`hw12/homework12.py`](hw12/homework12.py) | CSV | Student records in `files/students.csv` with `csv.DictReader`/`DictWriter`: add (no duplicate IDs, sorted), read (all or by ID), average mark per subject, update a mark |
| 13 | [`hw13/hw13.py`](hw13/hw13.py) | OOP: classes, inheritance | `Car` with a class-level counter, `age_of_car()` and a `@classmethod`, and an `ElectricCar` subclass with battery info |
| 14 | [`hw14/hw14.py`](hw14/hw14.py) | OOP: dunder methods, properties | `Vector` with `__add__`/`__str__`, `Book` with `__eq__`, and `Car` with `__new__` and validating `@property` setters |

## Notes

- `hw11` creates `test.json` and `hw12` creates `files/students.csv` in the **current working directory**.
- `hw13/hw13.py` only defines the classes and has no demo code. Import it to try it out:

  ```python
  from hw13 import Car, ElectricCar
  tesla = ElectricCar("Tesla", "Model 3", 2020, 12)
  tesla.car_info()
  tesla.battery_info()
  Car.total_cars()
  ```
