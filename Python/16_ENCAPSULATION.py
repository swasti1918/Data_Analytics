# =========================
# 1. Basic Encapsulation
# =========================
class Student:
    def __init__(self, name, marks):
        self.name = name        # Public
        self._marks = marks     # Protected
        self.__grade = "A"      # Private

    def show(self):
        print("Name:", self.name)
        print("Marks:", self._marks)
        print("Grade:", self.__grade)

print("---- Basic Encapsulation ----")
s1 = Student("Sam", 90)
s1.show()


# =========================
# 2. Accessing Private (Error Example)
# =========================
print("\n---- Private Access Test ----")
# print(s1.__grade)   # ❌ ERROR (uncomment to see error)


# =========================
# 3. Getter & Setter
# =========================
class Student2:
    def __init__(self, marks):
        self.__marks = marks   # Private

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, value):
        if value >= 0:
            self.__marks = value
        else:
            print("Invalid Marks")

print("\n---- Getter & Setter ----")
s2 = Student2(80)
print("Marks:", s2.get_marks())

s2.set_marks(95)
print("Updated Marks:", s2.get_marks())


# =========================
# 4. Encapsulation using Property
# =========================
class Student3:
    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value >= 0:
            self.__marks = value
        else:
            print("Invalid Marks")

print("\n---- Property Example ----")
s3 = Student3(70)
print("Marks:", s3.marks)

s3.marks = 90
print("Updated Marks:", s3.marks)


# =========================
# 5. Name Mangling (Advanced)
# =========================
print("\n---- Name Mangling ----")
# Accessing private variable using special syntax
print(s1._Student__grade)   # Not recommended but possible


# =========================
# 6. Real-Life Example (ATM)
# =========================
class ATM:
    def __init__(self, balance):
        self.__balance = balance   # Private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

print("\n---- ATM Example ----")
atm = ATM(1000)
atm.deposit(500)
atm.withdraw(300)
print("Balance:", atm.get_balance())