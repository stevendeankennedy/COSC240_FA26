'''
    Example for strings
    
    Authors:
        Michael R., Dusty, Bailey, Madison, Trent, Cole
'''

# Hans Christian Anderson
#   -> Anderson, H.C.

# Jack Skellington
#   -> Skellington, J.

#name = "Georgios Kyriacos Panayiotou"
#name = "John Jacob Jingleheimer Schmidt"
#name = "Jack Skellington"
name = "John"
parts = name.split()

# testing stuff goes here
#print(parts)
#print(parts[-1]) # this gives us the last name

the_new_name = '?'
# if name is 2, do this
if len(parts) < 2:
    print("Sorry, can't format your name")
else: # if name is more than 2, do this
    # split names, then find the first initial for each part
    #   (all but the last name)

    the_new_name = parts[-1] + ', '
    
    # probably need a loop with some kind of counting...
    i = 0
    while i < len(parts)-1:
        this_name = parts[i]
        print(this_name[0])
        print(parts[i])
        the_new_name = the_new_name + this_name[0] + '.'
        i += 1
    
    

print("Here you go:", the_new_name)










