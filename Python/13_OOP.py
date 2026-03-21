class Factory:
    a = 10  # Class attribute (shared by all objects)

    def hello(self):  
        # Instance method (works with object, takes 'self')
        print("How are you") 


obj = Factory()
print(obj.a)   # Accessing class attribute using object
obj.hello()    # Calling instance method


class Student:
    def __init__(self, name, age):
        # Constructor (called automatically when object is created)
        self.name = name   # Instance attribute (unique for each object)
        self.age = age

    def show(self):
        # Instance method
        print(f"YOUR NAME IS {self.name} AND AGE IS : {self.age}")
        

s1 = Student("sam", 21)
s2 = Student("swasti", 21)

print(s1.name, s1.age)  # Accessing instance attributes
print(s2.name, s2.age)

s1.show()
s2.show()


class Animal:
    name = "lion"  # Class attribute (same for all objects)

    def __init__(self, breed):
        self.breed = breed  # Instance attribute (different for each object)

    def show(self):
        # Instance method
        print("How are you")
    
    @classmethod    
    def hello(cls): 
        # Class method (works with class, uses 'cls')
        print("HEY THERE!")

    @staticmethod   
    def static():
        # Static method (no self, no cls — independent utility method)
        print("HOW ARE YOU")