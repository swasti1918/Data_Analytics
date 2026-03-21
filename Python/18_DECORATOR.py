# This is a decorator function
def my_decorator(func):
    
    # Wrapper function adds extra functionality
    def wrapper():
        print("Something before the function runs.")  # Code before original function
        
        func()   # Calling the original function
        
        print("Something after the function runs.")   # Code after original function
    
    return wrapper   # Returning the wrapper function


# Applying decorator to this function
@my_decorator
def say_hello():
    print("Hello!")   # Original function


# Calling the function
say_hello()