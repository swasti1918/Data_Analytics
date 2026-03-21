# ==============================
# DATA STRUCTURES IN PYTHON
# ==============================

# 1. LIST (ordered, mutable)
my_list = [1, 2, 3, 4]

print("List:", my_list)

# Add element
my_list.append(5)
print("After append:", my_list)

# Remove element
my_list.remove(2)
print("After remove:", my_list)

# Access element
print("First element:", my_list[0])

# ==============================
# 2. TUPLE (ordered, immutable)
# ==============================

my_tuple = (10, 20, 30)

print("\nTuple:", my_tuple)

# Access element
print("First element:", my_tuple[0])

# ==============================
# 3. SET (unordered, unique)
# ==============================

my_set = {1, 2, 3, 3, 4}

print("\nSet:", my_set)

# Add element
my_set.add(5)
print("After add:", my_set)

# Remove element
my_set.remove(1)
print("After remove:", my_set)

# ==============================
# 4. DICTIONARY (key-value pair)
# ==============================

my_dict = {"name": "Sanyam", "age": 20}

print("\nDictionary:", my_dict)

# Access value
print("Name:", my_dict["name"])

# Add/update value
my_dict["city"] = "Jaipur"
print("Updated dict:", my_dict)

# ==============================
# 5. STACK (using list)
# ==============================

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print("\nStack:", stack)

stack.pop()
print("After pop:", stack)

# ==============================
# 6. QUEUE (using list)
# ==============================

queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print("\nQueue:", queue)

queue.pop(0)
print("After dequeue:", queue)

# ==============================
# 7. STRING (as data structure)
# ==============================

text = "python"

print("\nString:", text)
print("Upper:", text.upper())
print("Slice:", text[0:3])