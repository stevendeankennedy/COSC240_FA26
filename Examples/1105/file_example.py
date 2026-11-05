'''
    File example
    Authors:
        Bailey, Cole, Michael R.
'''

# Reads the whole file
def version1(file):
    my_file = open(file) # create file object
    contents = my_file.read() # get the contents

    print(contents)

    my_file.close() # return os file resource

# Reads lines of a file
def version2(file):
    my_file = open(file) # create file object
    contents = my_file.readlines()
    
    print(contents)
    print("-----")
    print(contents[3])
    my_file.close() # return os file resource

def version3(file):
    print("opening...")
    with open(file, 'r') as myfile:
        #print(myfile)
        text = myfile.readline()
        text += myfile.readline()

        print("?->", text)

def write(words):
    f = open("words.txt", 'w')
    f.write(words)
    f.flush()
    f.close()

'''
    Read a csv file
    format:
    NAME,TYPE,LEGS
    Bark Vader,dog,4
    Meowly Cyrus,cat,4
'''

def getPets(file):
    f = open(file, 'r')
    pets = f.readlines()

    #print(pets)
    #print(pets[5])

    print(pets[0])

    my_pets = {
        "snoop dog" : "dog"
        }

    # iterate through each pet (skipping the header)
    for i in range(1, len(pets)):
        line = pets[i].split(',')
        num_legs = int(line[2][0])
        #print(f"{line[0]} has {line[2]} legs!")
        print(f"{line[0]} has {num_legs} legs!")
        my_pets[line[0]] = line[1]

    print(my_pets)






    

getPets("pets.csv")
#version3("pets.csv")
#write("hello world")
#write("goodbye")
