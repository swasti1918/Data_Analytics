# ==============================
# OPERATORS IN PYTHON
# ==============================

# 1. ARITHMETIC OPERATORS
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)        # float result
print("Floor Division:", a // b) # integer result
print("Modulus:", a % b)
print("Power:", a ** b)

# ==============================
# 2. COMPARISON OPERATORS
# ==============================

x = 5
y = 10

print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater:", x > y)
print("Less:", x < y)
print("Greater Equal:", x >= y)
print("Less Equal:", x <= y)

# ==============================
# 3. LOGICAL OPERATORS
# ==============================

p = True
q = False

print("AND:", p and q)
print("OR:", p or q)
print("NOT p:", not p)

# ==============================
# 4. ASSIGNMENT OPERATORS
# ==============================

n = 5
n += 3   # n = n + 3
print("n += 3:", n)

n -= 2
print("n -= 2:", n)

n *= 2
print("n *= 2:", n)

n /= 2
print("n /= 2:", n)

# ==============================
# 5. BITWISE OPERATORS
# ==============================

a = 5   # 0101
b = 3   # 0011

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT a:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

# ==============================
# 6. MEMBERSHIP OPERATORS
# ==============================

list1 = [1, 2, 3, 4]

print("2 in list:", 2 in list1)
print("5 not in list:", 5 not in list1)

# ==============================
# 7. IDENTITY OPERATORS
# ==============================

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is b:", a is b)     # False
print("a is c:", a is c)     # True
print("a == b:", a == b)     # True