# a decorator is a function, that takes a function as an input, 
# and returns a modified version as an output
def announce(f):
    def wrapper():
        print("About to run the function...") # a warning that its about to run the function
        f()                                   # actually run the function
        print("Done with the function.")      # tells you youve finished the function
    return wrapper 
# this is called a decorator

@announce #adding the announce decorator to this function
def hello():
    print("Hello, World!")
    
hello() 

# as we can see it prints the wrappers 'about to run function'
# followed by our hello() function
# followed again by the wrappers 'done with the function'

# this works, because hello() is wrapped inside the announce() function

