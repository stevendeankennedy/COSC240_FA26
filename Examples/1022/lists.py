'''
    Basic list stuff
    Authors:
        Bailey, Lark, Michael R, Cole, Declan
'''

# insert an element into the list
def insert(x, the_list, idx):
    print(the_list)
    # move elements after idx down
    i = len(the_list) - 2
    while i >= idx:
        the_list[i+1] = the_list[i]
        i -= 1
        
    # put x into the new empty spot (where idx was)
    the_list[idx] = x
    print(the_list)

# sort the_list using the bubble sort algo
def bubblesort(the_list):

    # bubble: start at beginning
    #for num in the_list:  # <- this is the cute python way
    for i in range(len(the_list)):
        # bubble: compare AND move n-1 times (resets after)
        for left in range(len(the_list)-1):
            # first number = left of bubble
            # second number = right of bubble
            # sort those 2 numbers (may need to swap or not)
            # if first > second, swap
            # bubble moves forward
            if the_list[left+1] < the_list[left]:
                swap(left, left+1, the_list)

# swap two things in this list
# tip from THE ORACLE ooooooohhh... maybe know this
def swap(left, right, the_list):
    tmp = the_list[right]
    the_list[right] = the_list[left]
    the_list[left] = tmp
    

nums = ['a', 'b', 'c', 'd', 'e', 'f', ' ']
insert('x', nums, 6)

print("bubble sort")
nums = [9, 8, 7, 1, 4, 6]
# test swap method
#swap(0, 1, nums)
#print(nums)

bubblesort(nums)
print(nums)
