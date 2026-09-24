'''
    FOR loops
'''

# basic for loop examples with containers

my_list = [22,44,88,10,12,14,16,18,20]

for i in my_list:
    print(i, end=" ")

print("!")

name = "Bear Grylls"

for letter in name:
    print(letter, end=", ")
print("is cool!")

my_dict = {
    "name" : "Bear",
    "age"  : 25,
    "food" : "worms"
}

for key in my_dict:
    print(key, my_dict[key])


# for loops using range
print("RANGE FUNCTION EXAMPLES... vvv")
N = 5 # number of times
for i in range(N):
    print(i, end=" ")
    print(name[i])
print()

N = 20
for i in range(3, N):
    print(i, end=" ")
print()

print("skip")
for i in range(2, N, 2):
    print(i, end=" ")
print()

print("negative")
for i in range(N, 2, -2):
    print(i, end=" ")
print()


# ---------------------------
print("Nested loops!")
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
print()






























