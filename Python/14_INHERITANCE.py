# =========================
# 1. Single Inheritance
# =========================
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

print("---- Single Inheritance ----")
d = Dog()
d.speak()   # inherited
d.bark()


# =========================
# 2. Multilevel Inheritance
# =========================
class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(B):
    def print_data(self):
        print("Class C")

print("\n---- Multilevel Inheritance ----")
c = C()
c.show()
c.display()
c.print_data()


# =========================
# 3. Multiple Inheritance
# =========================
class Father:
    def skill1(self):
        print("Father: Driving")

class Mother:
    def skill2(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Child: Coding")

print("\n---- Multiple Inheritance ----")
ch = Child()
ch.skill1()
ch.skill2()
ch.skill3()


# =========================
# 4. Hierarchical Inheritance
# =========================
class Parent:
    def home(self):
        print("Parent's House")

class Son(Parent):
    def bike(self):
        print("Son's Bike")

class Daughter(Parent):
    def scooty(self):
        print("Daughter's Scooty")

print("\n---- Hierarchical Inheritance ----")
s = Son()
d = Daughter()
s.home()
s.bike()
d.home()
d.scooty()


# =========================
# 5. Method Overriding
# =========================
class Animal2:
    def sound(self):
        print("Animal sound")

class Dog2(Animal2):
    def sound(self):
        print("Dog barks")

print("\n---- Method Overriding ----")
d2 = Dog2()
d2.sound()


# =========================
# 6. super() Keyword
# =========================
class Animal3:
    def __init__(self):
        print("Animal Constructor")

class Dog3(Animal3):
    def __init__(self):
        super().__init__()
        print("Dog Constructor")

print("\n---- super() Example ----")
d3 = Dog3()