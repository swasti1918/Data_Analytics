# ==============================
# STRINGS IN PYTHON
# ==============================

# Creating strings
name = "Sanyam"
greeting = 'Hello'

print("Name:", name)
print("Greeting:", greeting)

# String indexing
print("First character:", name[0])
print("Last character:", name[-1])

# String slicing
print("First 3 letters:", name[0:3])

# String methods
text = "python programming"

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Length:", len(text))
print("Replace:", text.replace("python", "java"))

# String concatenation
full = greeting + " " + name
print("Full:", full)

# ==============================
# TYPE CONVERSION (TYPE CASTING)
# ==============================

# Integer to float
a = 10
b = float(a)
print("Int to Float:", b, type(b))

# Float to int
c = 5.9
d = int(c)
print("Float to Int:", d, type(d))

# Int to string
num = 100
str_num = str(num)
print("Int to String:", str_num, type(str_num))

# String to int
x = "50"
y = int(x)
print("String to Int:", y, type(y))

# String to float
p = "3.14"
q = float(p)
print("String to Float:", q, type(q))

