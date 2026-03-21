from functools import reduce   # reduce needs to be imported


# =========================
# 1. LAMBDA FUNCTION
# =========================
# One-line anonymous function

add = lambda a, b: a + b
print("Lambda Add:", add(5, 3))


# =========================
# 2. MAP FUNCTION
# =========================
# Applies function to each element

nums = [1, 2, 3, 4]

# Multiply each element by 2
double = list(map(lambda x: x * 2, nums))

print("Map (Double):", double)


# =========================
# 3. FILTER FUNCTION
# =========================
# Filters elements based on condition

nums = [1, 2, 3, 4, 5, 6]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))

print("Filter (Evens):", evens)


# =========================
# 4. REDUCE FUNCTION
# =========================
# Reduces list to single value

nums = [1, 2, 3, 4]

# Sum of all elements
total = reduce(lambda a, b: a + b, nums)

print("Reduce (Sum):", total)


# =========================
# 5. ADVANCED EXAMPLE
# =========================
nums = [1, 2, 3, 4, 5]

# Step 1: Square numbers
squared = list(map(lambda x: x*x, nums))

# Step 2: Filter even squares
even_squares = list(filter(lambda x: x % 2 == 0, squared))

# Step 3: Sum them
result = reduce(lambda a, b: a + b, even_squares)

print("Advanced Result:", result)