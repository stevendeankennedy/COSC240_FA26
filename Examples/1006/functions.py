'''
    Functions!

    Examples - How to make/ how to use!

    Authors: Quentin, Bailey, Ehren, Dusty
'''

# A simple message function
#   that prints hello
def hello(name):
    print("Hello,", name)
    # secret hidden return value - that returns void


# add a to b, and return result
def add(a,b): # a and b are arguments
    #result = a + b
    return a + b

# this is a function "stub"
def subtract(a,b):
    print("TODO")
    pass

def get_grade(number_grade):
    grade = "F" # variables in functions are called "local variable"
    if (number_grade >= 90):
        grade = "A"

    return grade

def get_values():
    return 1, 2, 3, 4
    
print("???")
hello("Jackson")
a = "This is a global variable"
result = add(1,1) # 1 and 1 are parameters
print(result)
result = add("hello", "world")
print(result)
#print(grade)

data = get_values()
print(data)
