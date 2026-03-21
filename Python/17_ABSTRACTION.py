from abc import ABC, abstractmethod


# =========================
# 1. Abstract Class & Method
# =========================
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass   # No implementation


class Dog(Animal):
    def sound(self):
        print("Dog barks")


print("---- Abstract Class Example ----")
d = Dog()
d.sound()


# =========================
# 2. Abstract Class with Constructor
# =========================
class Vehicle(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print(f"{self.name} starts with key")


print("\n---- Abstract with Constructor ----")
c = Car("BMW")
c.start()


# =========================
# 3. Multiple Abstract Methods
# =========================
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area:", self.l * self.b)

    def perimeter(self):
        print("Perimeter:", 2 * (self.l + self.b))


print("\n---- Multiple Abstract Methods ----")
r = Rectangle(4, 5)
r.area()
r.perimeter()


# =========================
# 4. Real-Life Example (Payment System)
# =========================
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class Card(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")


print("\n---- Payment System ----")
p1 = UPI()
p2 = Card()

p1.pay(1000)
p2.pay(2000)


# =========================
# 5. Cannot Create Object of Abstract Class
# =========================
print("\n---- Abstract Object Test ----")
# a = Animal()   # ❌ ERROR (cannot instantiate abstract class)