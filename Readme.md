# Simple Python Calculator

## Description

This project is a basic Python calculator that performs four arithmetic operations:

* Addition
* Subtraction
* Multiplication
* Division

The program uses **functions** to handle each mathematical operation. It also uses **error handling** to prevent the program from crashing when dividing by zero.

This project is useful for beginners learning:

* Python functions
* Conditional statements
* Error handling using `try` and `except`

---

## Features

* Performs basic calculations
* Uses separate functions for each operation
* Handles division by zero errors
* Simple and beginner-friendly structure

---

## Functions Used

### 1. Addition

Adds two numbers together.

### 2. Subtraction

Subtracts the second number from the first number.

### 3. Multiplication

Multiplies two numbers.

### 4. Division

Divides the first number by the second number.
Includes error handling to avoid division by zero.

---

## Example Code Structure

```python
def sub(a, b):
    if opp == '-':
        print(a - b)

def mult(a, b):
    if opp == '*':
        print(a * b)

def divisible(a, b):
    try:
        if opp == '/':
            print(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
```

---

## How to Run the Program

1. Install Python on your computer.
2. Save the file as `calculator.py`.
3. Open a terminal or command prompt.
4. Run the program:

```bash
python calculator.py
```

---

## Possible Improvements

Future versions of this project could include:

* User input using `input()`
* A loop so the calculator runs continuously
* A menu for choosing operations
* Cleaner function structure

---

## Learning Goal

The goal of this project is to help beginners practice:

* Writing Python functions
* Using conditions (`if` statements)
* Handling errors with `try` and `except`

---

## Author

Created as a **Python beginner practice project**.
