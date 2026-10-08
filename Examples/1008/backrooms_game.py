'''
    Examples of functions PART 2!

    Simple BACK-ROOMS game where a character collects stuff

    Authors:
        Dusty, Bailey, Cole, Ehren, Michael R, Declan, Casey
'''

# constants go near the top (usually 2nd, after imports)
NEEDED_POINTS = 4

# some rooms
rooms = ["gold coin", "watch", "yeezies", "hat"]

# person, with name and stuff
backpack = []
person = {
    "name" : "Clark",
    "inv" : backpack,
    "points" : 0,
    "pos" : 0
    }

# play_game()?
def play_game():
    # repeat:
    while person["points"] < NEEDED_POINTS:
        print(rooms)
        print(person["inv"])
        # move player
        num_steps = int(input("How many steps?>"))
        move(num_steps)
        # collect item
        item = collect_item(person["pos"])
        backpack.append(item)
        person["points"] += 1

# collect item()? <- put item in the bag
def collect_item(pos):
    the_item = rooms[pos]
    return the_item

# move player()?
def move(step):
    # don't let player leave the backrooms!
    if (step + person["pos"] >= len(rooms)):
        print("Can't leave the backrooms!")
        person["pos"] = 0
        return
    person["pos"] = person["pos"] + step

'''
    Testing functions below vvv
'''

def test_move(s):
    print(person)
    move(1)
    print(person)
    move(s)
    print(person)

def test_backpack():
    print("What's in the pack?")
    print(backpack)
    #play_game()
    #print(backpack)

# Run the game
play_game()
test_move(3)
test_backpack()











    
