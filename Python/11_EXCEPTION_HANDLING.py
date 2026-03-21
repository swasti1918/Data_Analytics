# ==============================
# EXCEPTION HANDLING IN PYTHON
# ==============================

# 1. Basic try-except
try:
    a = int(input("Enter a number: "))
    b = 10 / a
    print("Result:", b)
except:
    print("Error occurred!")

# ==============================
# 2. Catch specific exception
# ==============================

try:
    x = int("abc")
except ValueError:
    print("ValueError: Cannot convert string to int")

# ==============================
# 3. Multiple exceptions
# ==============================

try:
    a = int(input("Enter number: "))
    result = 10 / a
    print(result)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ==============================
# 4. else block
# ==============================

try:
    num = int(input("Enter number: "))
except ValueError:
    print("Wrong input")
else:
    print("You entered:", num)

# ==============================
# 5. finally block
# ==============================

try:
    print("Trying...")
    x = 5 / 1
except:
    print("Error")
finally:
    print("This will always execute")

# ==============================
# 6. raise keyword
# ==============================

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise Exception("Underage not allowed")
    print("Access granted")
except Exception as e:
    print("Error:", e)

# ==============================
# 7. Custom exception
# ==============================

class MyError(Exception):
    pass

try:
    num = -1
    if num < 0:
        raise MyError("Negative value not allowed")
except MyError as e:
    print("Custom Error:", e)