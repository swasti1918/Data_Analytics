# =========================
# 1. Method Overloading (Using Default Arguments)
# =========================
class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

print("---- Method Overloading ----")
m = Math()
print(m.add(5, 10))        # 2 arguments
print(m.add(5, 10, 15))    # 3 arguments


# =========================
# 2. Method Overriding
# =========================
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

print("\n---- Method Overriding ----")
d = Dog()
d.sound()


# =========================
# 3. Operator Overloading
# =========================
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def show(self):
        print(self.x, self.y)

print("\n---- Operator Overloading ----")
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2   # calls __add__
p3.show()


# =========================
# 4. Duck Typing
# =========================
class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")

def make_fly(obj):
    obj.fly()

print("\n---- Duck Typing ----")
b = Bird()
a = Airplane()
make_fly(b)
make_fly(a)


# =========================
# 5. Polymorphism with Functions
# =========================
print("\n---- Polymorphism with Functions ----")
print(len("Hello"))        # string
print(len([1, 2, 3, 4]))   # list
print(len((1, 2)))         # tuple