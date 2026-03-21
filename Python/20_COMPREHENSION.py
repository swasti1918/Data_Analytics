# =========================
# 1. LIST COMPREHENSION
# =========================

# Create list of squares from 1 to 5
list_squares = [x*x for x in range(1, 6)]  # x*x = expression

print("List Comprehension (Squares):", list_squares)


# =========================
# 2. SET COMPREHENSION
# =========================

# Create set of even numbers (duplicates automatically removed)
set_evens = {x for x in range(10) if x % 2 == 0}  # condition applied

print("Set Comprehension (Evens):", set_evens)


# =========================
# 3. DICTIONARY COMPREHENSION
# =========================

# Create dictionary: number → square
dict_squares = {x: x*x for x in range(1, 6)}  # key:value pair

print("Dictionary Comprehension (Squares):", dict_squares)


# =========================
# 4. WITH CONDITION (FILTER)
# =========================

# Only odd numbers squares
odd_squares = [x*x for x in range(10) if x % 2 != 0]

print("Odd Squares (List):", odd_squares)


# =========================
# 5. STRING EXAMPLE
# =========================

word = "hello"

# Unique characters using set comprehension
unique_chars = {c for c in word}

print("Unique Characters (Set):", unique_chars)


# =========================
# 6. ADVANCED (IF-ELSE)
# =========================

# Label numbers as Even/Odd using dictionary
even_odd = {x: ("Even" if x % 2 == 0 else "Odd") for x in range(1, 6)}

print("Even/Odd Dictionary:", even_odd)