'''
    Study Guide

    Note: this is not exhaustive.  Please use your book,
        your notes, and your programming assignments
        to prepare for the exam Thursday (10/1).

    General exam format (subject to change!):
        - 10-20 or so multiple choice
        - 2-5 concepts questions (short answer)
        - 1-3 programming questions (similar to zyBooks labs)
    Authors:
        Steve, Cole, Bailey, Dusty, Jackson, Declan, 
        Michael R and friends
'''

# Chapter 1 -----------------------------
# Terminology - input, output, process, interpreter,
#   statement, expression, variable, assignment, comments
#   string, newline, type, syntax, syntat error, runtime error,
#   whitespace
# Key concepts - error checking, basic Python
# Notes - a lot of terminology in this chapter, but otherwise
#   not super important for the exam

# Chapter 2 ------------------------------
# Terminology - variable, assignment statement, incrementing,
#   identifier, numberic types: int, float, literal, operator,
#   expression, evaluate
# Key concepts - assignment variables, how they work, where
#   they go, etc.

# example variables
my_name = "Jamiroquai"
my_other_name = input("Your name? >")
# identifier/variable <- data

# Chapter 3 ------------------------------
# Terminology - string, sequence type, concatenation,f-strings,
#   container, list, element, set, tuple, dictionary
# Key concepts - type conversion (implicit vs explicit)

# examples
words = "six" + "seven" # result is "sixseven"

# Chapter 4 ------------------------------
# Terminology - branch, if, if-else, equality (==) and other operations,
#   relational operator, logical operator, boolean, in/not in, code blocks
# Key concepts - branching logic***, section 4.5, 4.6, 4.7

# examples
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
if (a > b):
    if (c > d):
        if (e > f):
            print("ef block")
        print("cd block")
    print("ab block")
    
# Chapter 5 -------------------------------
# Terminology - loops, while, for, loop variable (i), 
# Key concepts - iterating through a container class (e.g. print all elements in a list 1 by 1)

# examples
my_list = [6, 7, 67, 6677, 666777, 6767, 676767] #btw, I'm so funny hahahahahahahahah

# printing them all, not using a loop (aka the lazy / maybe bad, but definitely bad for the exam way
print(my_list)

print("while:")
# printing them all, using while
i = 0
while i < len(my_list):
    print(f"{i}:{my_list[i]}")
    i = i + 1
    # i += 1 # alternative style

print("for:")
# printing them all, using for
for element in my_list:  # "for each"
    print(element)

print("for v2:")
for i in range(len(my_list)): # "real" for loop
    print(f"{i}:{my_list[i]}")




















