# *args → used to pass multiple values as a tuple
def add(*args):
    sum = 0   # Initialize sum to 0
    
    # Loop through all values passed in args
    for i in args:
        sum = sum + i   # Add each value to sum
    
    print(sum)   # Print final result


# Calling function with multiple arguments
add(10, 20, 30, 40)



# **kwargs → used to pass multiple key-value pairs as a dictionary
def info(**kwargs):
    
    # Loop through keys in dictionary
    for i in kwargs:
        # i = key, kwargs[i] = value
        print(f"{i} : {kwargs[i]}")


# Calling function with key-value arguments
info(name="sam", age=20, city="Begun")