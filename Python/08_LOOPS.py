# ==============================
# LOOPS IN PYTHON
# ==============================

# 1. FOR LOOP (basic)
print("For loop:")
for i in range(5):
    print(i)   # 0 to 4

# ==============================
# 2. FOR LOOP WITH RANGE
# ==============================

print("\nRange with start, stop, step:")
for i in range(1, 10, 2):
    print(i)   # 1,3,5,7,9

# ==============================
# 3. LOOP THROUGH STRING
# ==============================

name = "Sanyam"
for ch in name:
    print(ch)

# ==============================
# 4. WHILE LOOP
# ==============================

print("\nWhile loop:")
count = 1

while count <= 5:
    print(count)
    count += 1

# ==============================
# 5. BREAK STATEMENT
# ==============================

print("\nBreak example:")
for i in range(10):
    if i == 5:
        break
    print(i)

# ==============================
# 6. CONTINUE STATEMENT
# ==============================

print("\nContinue example:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# ==============================
# 7. PASS STATEMENT
# ==============================

print("\nPass example:")
for i in range(3):
    pass   # does nothing

# ==============================
# 8. NESTED LOOP
# ==============================

print("\nNested loop:")
for i in range(3):
    for j in range(3):
        print(i, j)

# ==============================
# 9. USER INPUT EXAMPLE
# ==============================

n = int(input("\nEnter number: "))

sum = 0
for i in range(1, n + 1):
    sum += i

print("Sum from 1 to n:", sum)