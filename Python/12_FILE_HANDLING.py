# ==============================
# FILE HANDLING IN PYTHON
# ==============================

# 1. WRITE TO FILE (creates file if not exists)
file = open("demo.txt", "w")
file.write("Hello Sanyam\n")
file.write("Learning Python File Handling")
file.close()

# ==============================
# 2. READ FILE
# ==============================

file = open("demo.txt", "r")
content = file.read()
print("\nFile Content:\n", content)
file.close()

# ==============================
# 3. READ LINE BY LINE
# ==============================

file = open("demo.txt", "r")
for line in file:
    print("Line:", line.strip())
file.close()

# ==============================
# 4. APPEND DATA
# ==============================

file = open("demo.txt", "a")
file.write("\nThis is appended text")
file.close()

# ==============================
# 5. USING WITH (BEST PRACTICE)
# ==============================

with open("demo.txt", "r") as file:
    print("\nUsing with:\n", file.read())

# ==============================
# 6. FILE MODES
# ==============================

# "r" → read
# "w" → write (overwrite)
# "a" → append
# "x" → create (error if exists)
# "b" → binary mode

# ==============================
# 7. CHECK FILE EXISTS
# ==============================

import os

if os.path.exists("demo.txt"):
    print("\nFile exists")
else:
    print("\nFile does not exist")

# ==============================
# 8. DELETE FILE
# ==============================

# os.remove("demo.txt")   # Uncomment to delete file