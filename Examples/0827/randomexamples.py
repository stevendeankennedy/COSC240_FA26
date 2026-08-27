print("-----\n|   |\n-----")

a = 2
b = 1

print(a + b)

#userinput = input(">>>")
#userinput = int(userinput)
#print("you entered", userinput)

#print(1 + 1)
#print(userinput + 1)



'''
    Program to calculate how much money you
        made per hour.

    Special thanks to: Lark, Michael, Tyler, Cole
'''

# divide total money by number of hours, thanks Michael R
total = input("How much money did you make? >")
total = float(total)

hours = input("How many hours did you work? >")
hours = float(hours)

per_hour = total / hours

#print(per_hour) #<--- old version of print, very basic

# new and better 'formatted string' printing
print(f'You made ${per_hour:.2f} per hour')
