#this file connects, references, to functions.py
from functions import square
#this is importing a specific function from within a module

for i in range(10):
    print(f"The square of {i} is {square(i)}")
