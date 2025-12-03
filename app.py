"""
Python Practice - Comprehensive Guide
This file covers fundamental Python concepts with examples and explanations.
"""

# ============================================
# 1. VARIABLES AND DATA TYPES
# ============================================

# Integer - whole numbers
student_count = 1000

# Float - decimal numbers
rating = 4.33

# Boolean - True or False values
is_published = False

# String - text data
course_name = "Python Programming"

# Printing variables
print("Total number of students:", student_count)


# ============================================
# 2. STRING FORMATTING
# ============================================

# F-strings (formatted string literals) - modern way to format strings
course = "Python Programming"
message = f"Course '{course}' has been published successfully!"
print(message)


# ============================================
# 3. STRING OPERATIONS
# ============================================

# String length and indexing
course = "Python Programming"
print(len(course))  # Length of string
print(course[-1])   # Last character (negative indexing)

# String slicing [start:end]
print(course[0:3])  # Characters from index 0 to 2
print(course[0:])   # From index 0 to end
print(course[:])    # Entire string (copy)
print(course[:3])   # From beginning to index 2

# Escape sequences
course = 'Python " Programming'      # Double quotes inside single quotes
course = 'Python \" Programming'     # Escaping quotes with backslash
course = 'Python \n Programming'     # \n creates new line
print(course)


# ============================================
# 4. STRING CONCATENATION
# ============================================

first_name = "John"
last_name = "Doe"

# Method 1: Using + operator
full_name = first_name + " " + last_name
print(full_name)

# Method 2: F-strings (preferred)
full_name = f"{first_name} {last_name}"
print(full_name)

# F-strings with expressions
full_name = f"{len(first_name)} {last_name}"
print(full_name)


# ============================================
# 5. STRING METHODS
# ============================================

course = "     Python Programming"

print(course.upper())           # Convert to uppercase
print(course.lower())           # Convert to lowercase
print(course.title())           # Capitalize first letter of each word
print(course.strip())           # Remove leading/trailing whitespace
print(course.find("Pro"))       # Find substring index (-1 if not found)
print(course.replace("P", "J")) # Replace substring
print("pro" in course)          # Check if substring exists (returns bool)


# ============================================
# 6. NUMERIC DATA TYPES
# ============================================

x = 1       # Integer
x = 1.1     # Float
x = 1+2j    # Complex number


# ============================================
# 7. ARITHMETIC OPERATORS
# ============================================

print(10/3)   # Division - returns float (3.333...)
print(10//3)  # Floor division - returns integer (3)
print(10**3)  # Exponentiation - power (1000)

# Augmented assignment operators
x = 10
x += 3  # Shorthand for x = x + 3
print(x)


# ============================================
# 8. MATH MODULE
# ============================================

import math

print(round(2.9))       # Round to nearest integer
print(abs(-2.9))        # Absolute value (remove negative)
print(math.ceil(2.2))   # Round up to nearest integer


# ============================================
# 9. USER INPUT
# ============================================

# Get user input (always returns string)
x = input("Enter your name: ")

# Type conversion - convert string to integer
y = int(x) + 1
print(y)

# Using input in strings
print(f"Hello {x}")
print("Hello" + x)


# ============================================
# 10. STRING SLICING PRACTICE
# ============================================

name = "abraham"
print(name[1:4])  # Extract 'bra' (index 1 to 3)


# ============================================
# 11. CONDITIONAL STATEMENTS
# ============================================

# If/elif/else structure
temperature = 29

if temperature > 30:
    print("It's a hot day")
elif temperature < 30:
    print("It's a cold day")
else:
    print("It's a lovely day")

print("done")  # Code outside if block always executes


# ============================================
# 12. TERNARY OPERATOR
# ============================================

age = 20

# Traditional if/else
if age >= 18:
    message = "You are eligible to vote"
else:
    message = "You are not eligible to vote"

# Ternary operator (one-line conditional)
# Syntax: value_if_true if condition else value_if_false
message = "You are eligible to vote" if age >= 18 else "You are not eligible to vote"
print(message)


# ============================================
# 13. LOGICAL OPERATORS
# ============================================

# Combining conditions with and, or, not
high_income = True
good_credit = False
student = True

if (high_income or good_credit) and not student:
    print("Eligible for loan")


# ============================================
# 14. COMPARISON OPERATORS
# ============================================

# Traditional comparison
age = 22
if age >= 15 and age <= 65:
    print("Eligible for work")

# Chaining comparison (Pythonic way)
age = 22
if 15 <= age <= 65:
    print("Eligible for work")


# ============================================
# 15. FOR LOOPS
# ============================================

# range(start, stop, step)
for number in range(1, 5, 2):
    print("ATTEMPT", number, (number) * ".")

# For loop with break
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    # Else block executes if loop completes without break
    print("Attempted 3 times and failed")

# Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Iterating over different types
for x in range(5):
    print(x)

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)


# ============================================
# 16. WHILE LOOPS
# ============================================

# While loop - continues until condition is false
command = ""
while command.lower() != "quit":
    command = input("enter command:")
    print("ECHO", command)


# ============================================
# 17. FUNCTIONS
# ============================================

# Basic function definition
def greet():
    print("Hello")
    print("Welcome aboard")

greet()  # Function call


# Function with parameters
def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard")

greet("abraham", "lincoln")


# Function with return value
def multiply(number1, number2):
    return number1 * number2

print(multiply(3, 4))


# Function with variable number of arguments (*args)
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4))
