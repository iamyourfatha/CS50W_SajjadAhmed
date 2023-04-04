import functions
#this is importing the entire module
#if you do not specify what you ase importinh
# from functions import squares

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")
    #then you have to specify it in the function you need it for
    # functions.square : the file.function that your importing

