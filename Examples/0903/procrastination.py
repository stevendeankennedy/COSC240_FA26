'''
    Program to calculate how much time
    I could be wasting.

    Authors: Steve K & Friends
    Special Thanks:
        Dusty, Cole, Juaquim, Madison, Declan, Lark,
        Trent, Bailey
    9/3/2026
'''

print("Welcome to the procrastination calculator!")

# Constants
TIKTOK_MINS = 0.5
NAP_MINS = 20
SPIDERVERSE_RUNTIME = 117

# get input
num_assignments = int(input("Number of assignments? >"))
mins_per_assignment = int(input("How long will they each take? >"))

# figure out what we could do with that time
total_minutes = num_assignments * mins_per_assignment
num_spiderverses = total_minutes // SPIDERVERSE_RUNTIME
num_tiktoks = total_minutes / TIKTOK_MINS
naptime = total_minutes // NAP_MINS



# print out results
print(f"\nYou have {total_minutes} minutes of work to do!")
print(f"\t... instead of working, you could:")
print(f"Watch Spider-Man {num_spiderverses} times!")
print(f"You could take {naptime} naps!")
print(f"Or you could doomscrool for {total_minutes} minutes, watching {num_tiktoks:.0f} TikToks!")








