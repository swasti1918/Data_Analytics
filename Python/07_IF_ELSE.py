# ==============================
# IF ELSE IN PYTHON
# ==============================

# 1. Simple if
age = 18

if age >= 18:
    print("You are eligible to vote")

# ==============================
# 2. if - else
# ==============================

num = 7

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ==============================
# 3. if - elif - else
# ==============================

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# ==============================
# 4. Nested if
# ==============================

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed entry")
    else:
        print("ID required")
else:
    print("Underage")

# ==============================
# 5. Short-hand if (one line)
# ==============================

x = 10

if x > 5: print("x is greater than 5")

# ==============================
# 6. Short-hand if-else (Ternary)
# ==============================

y = 4
result = "Even" if y % 2 == 0 else "Odd"
print(result)

# ==============================
# 7. User Input Example
# ==============================

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")