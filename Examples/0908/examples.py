'''
    Some Python examples.  Don't need to turn this in.
    Sept 8
'''

# strings
str1 = "hello"
str2 = "world"
str3 = str1 + str2
print(str3)
#str1[0] = "X"

# lists
my_list = [0, 10, 100, "1000", 10000]
print(my_list)
print(my_list[2])

my_list[3] = 1000
print(my_list)
my_list.pop(2)
print(my_list)
#my_list.remove("1000")  # <- there's no actual "1000" str
my_list.remove(1000)
print(my_list)

# tuples
my_tuple = ('a', 'b', 'c')
print(my_tuple)
#my_tuple[0] = 'X'  # <-  NO, tuples are not mutable

# sets
num_set = {1, 2, 3, 4, 5}
num_set2 = set([1, 2, 3])
print(num_set)
print(num_set2)

# dictionary - special container type that associates
                # keys to values

pet_dict = {
    "steve": "dog",
    "ash": "pikachu",
    "mickey": "Pluto",
    "alex": "wolf"
    }

print(pet_dict)
print(pet_dict["steve"]) # the key-value pair for steve
print(pet_dict["alex"])
pet_dict["steve"] = "snake"
print(pet_dict["steve"]) # the key-value pair for steve
del pet_dict["alex"]
print(pet_dict)



'''
    OTHER TYPES -------------------------------------
'''

# numeric
x = 1 # int
y = 1.2 #float

# sequence - string, list, tuple

# container types - sequence types, and set, dict



'''
    Converting types ------------------
'''




































