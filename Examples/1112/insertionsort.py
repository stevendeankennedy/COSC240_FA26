'''
    Insertion Sort
    Authors: Declan, Bailey, Michael R, Alex
'''

def insertion_sort(my_list):
    # outer loop - look at every number
    for i in range(1, len(my_list)):
        # inner loop - insert them to the left
        print("->", i)
        j = i
        while(j > 0 and (my_list[j] < my_list[j - 1])):
            swap(my_list, j, j-1) #maybe?
            print("?", my_list)
            j = j - 1

def swap(my_list, a, b):
    tmp = my_list[a]
    my_list[a] = my_list[b]
    my_list[b] = tmp

nums = [10,1,9,2,3,8,7]
print(nums)
insertion_sort(nums)
print(nums)
