'''
    Practice with lists, sets, and dictionaries

    This program, first messes around with types, but
        then, it will create a dictionary of
        useful(ish) college things and their prices.
        Then it will calculate the costs of the
        student needs.

    Special thanks to: Bailey, Cole, Jackson, Trent,
        Dusty, Quentin
'''

# lists - have a bunch of ordered elements
# sets - unordered, unique elements
# dicts - group of key-value pairs

'''
    -------------------------------------------------
    Sets
'''

# room mates
mate1 = {"pizza", "ramen", "ice cream"}
mate2 = {"apple", "chips", "pizza"}

print("Welcome to the college life program!")

# union
my_union = mate1.union(mate2)

print(mate1)
print(mate2)
print("Union:", my_union)

my_union = mate1.intersection(mate2)
print("Intersection:", my_union)

# you don't need to study this one, but difference
my_union = mate1.difference(mate2)
print("Difference (set1 - set2)", my_union)

'''
    --------------------------------------------------
    Lists
'''

college_stuff = ["pizza", "alfredo", "chicken"]

print("The length is", len(college_stuff))
print("Element at index 2 is", college_stuff[2])

# put something at the end
college_stuff.append("water")
print(college_stuff)
college_stuff.pop(1)
print(college_stuff)
college_stuff.remove("water")
print(college_stuff)

college_stuff = college_stuff + list(mate2)
print(college_stuff)

print("Pizza can be found at:", college_stuff.index("pizza"))
college_stuff.remove("pizza")
print("Pizza can be found at:", college_stuff.index("pizza"))

'''
    ------------------------------------------------
    Dictionaries
    (main program really starts down here...)
'''

stuff = {
    "pizza": 2.75,
    "ramen": 2.00,
    "chicken": 6.50,
    "ice cream": 7.89,
    "poncho": 4.99,
    "apple": 0.99,
    "chips": 6.75,
    "alfredo": 14.36,
    "depleted plutonium": 3990.90
    }

# don't want to erase this so you can look at it...
#temp_result = stuff["pizza"] + stuff["ramen"]
#print(temp_result)

result = stuff[college_stuff[0]] + stuff[college_stuff[1]] + stuff[college_stuff[2]] + stuff[college_stuff[3]]

print("Oh, you would like", college_stuff, "?")
print(f'That will cost ${result:.02f}!')



'''
    One more dictionary for practice
'''

lyrics = {
    "du": "you",
    "bist": "are",
    "gut": "good",
    "genug": "enough"
    }

print(f'The song "Du Bist Gut Genug", my favorite song of all time, by the way... means:')
print(f'{lyrics["du"]} {lyrics["bist"]} {lyrics["gut"]} {lyrics["genug"]}')














