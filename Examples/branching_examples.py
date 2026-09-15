'''
    Examples with branching logic (and basic loop included
        for funsies).

    Special thanks to:
        
'''

# Temperature
temp = int(input("What temperature? >"))
if (temp > 80):
    print("That's hot!")
#if (temp > 50):   # <--- Be careful!  You might need elif
elif (temp > 50):    
    print("That's warm...")

# Letter grade
grade = float(input("What grade did you get? >"))
letter = 'F'

if grade > 89.44:
    letter = 'A'
elif grade > 79.99:
    letter = 'B'
elif grade > 69.99:
    letter = 'C'
elif grade > 59.99:
    letter = 'D'
elif grade >= 0:
    letter = 'F'
else:  # <-- defensive programming!  protect yourself
    letter = 'bad number'

print(f"{grade}?  That's a {letter}!")



'''
    Defines what kind of person and if they are
        allowed to use this software.
    Special thanks:
        Trent, Bailey, Rich, Declan
'''

age = int(input("What's your age? >"))
isOK = False
stage = "something"

# Can they use software?
if age > 17 and age < 36:
    isOK = True

# Are they a child, teenager, whatever?
if age > 0:
    stage = "baby"
if age > 5:
    stage = "child"
if age > 12:
    stage = "teenager"
if age > 18:
    stage = "adult"
if age > 35:
    stage = "unc"  # really????

print(f'You are a {stage}!')
#if (isOK == True):  # <-- isOK is a boolean
if(isOK):  # <-- booleans are already True/False
    print("You can use this app!")
else:
    print("Sorry, you can't use this app!!")
    


















