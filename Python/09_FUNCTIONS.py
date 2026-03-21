# ==============================
# FUNCTIONS IN PYTHON
# ==============================

# 1. Simple function
def greet():
    print("Hello, welcome!")

greet()

# ==============================
# 2. Function with parameters
# ==============================

def add(a, b):
    print("Sum:", a + b)

add(5, 3)

# ==============================
# 3. Function with return value
# ==============================

def multiply(x, y):
    return x * y

result = multiply(4, 5)
print("Multiplication:", result)

# ==============================
# 4. Default parameters
# ==============================

def greet_user(name="Guest"):
    print("Hello,", name)

greet_user()
greet_user("Sanyam")

# ==============================
# 5. Keyword arguments
# ==============================

def student(name, age):
    print("Name:", name, "Age:", age)

student(age=20, name="Sanyam")

# ==============================
# 6. Arbitrary arguments (*args)
# ==============================

def total_sum(*numbers):
    print("Sum:", sum(numbers))

total_sum(1, 2, 3, 4)

# ==============================
# 7. Arbitrary keyword arguments (**kwargs)
# ==============================

def details(**info):
    print(info)

details(name="Sanyam", age=20, city="Jaipur")

# ==============================
# 8. Lambda function (anonymous)
# ==============================

square = lambda x: x * x
print("Square:", square(5))

# ==============================
# 9. Recursive function
# ==============================

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))