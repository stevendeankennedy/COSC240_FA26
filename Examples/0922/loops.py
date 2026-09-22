'''
    LLLOOOOPPPSSS!!!

    This example code demonstrates while and for loops.

    Authors:
        Steve K, Cole, Trent, Lark, Ehren, Declan, Michael,
        Dusty, Korbin, Bailey, 
'''

# basic while loop
'''
This is an infinite loop.  Don't do this, BUT
    if you end up in an inf loop, press CTRL+C
while True:
    print("hello")
'''

MAX_COUNT = 5

word = "word"
count = 1
while count <= MAX_COUNT:
    count += 1
    print(word)

# print 1-5
count = 1
while count <= MAX_COUNT:
    print(count)
    count += 1

# print odds
count = 0
while count <= MAX_COUNT:
    print(count)
    count += 2

'''
    Prints numbers from start to end
    it will say whether the number is even or odd.
'''

print("Evens and odds")
start = int(input("First number >"))
end = int(input("Last number >"))

num = start
while num <= end:
    #print(num)
    even_or_odd = "odd"
    if num % 2 == 0:
        even_or_odd = "even"
    #else:
    #    print(f"{num} is odd")

    print(f"{num} is {even_or_odd}")
    num += 1

names = ["Bilbob", "Fredorio", "Alicat", "Dominiquo", "Newman"]
print(names)

i = 0
length = len(names)
while i < length:
    print(names[i])
    i += 1
    #print(i)

# SEQUENTIAL SEARCH
# AKA LINEAR SEARCH

i = 0
isFound = False
target = input("What cat are you looking for? >")
while i < len(names) and not isFound:
    if names[i] == target:
        print(f"I found {target} at {i}!")
        isFound = True
    i += 1
if not isFound:
    print(f"Sorry, I lost {target}...")



'''
    Convert a decimal number to binary
'''

num = int(input("Enter a number to turn to binary >"))

while num > 0:
    #print(f"??->{num}")
    b_digit = num % 2   # the actual binary
    num = num // 2  # total
    print(b_digit)

# Tip from Michael R: we can add these digits to a string




'''
    Last example, print a list in reverse.
'''

nums = [8,7,6,5,4,3,2,1]
reverse_nums = []

i = len(nums) - 1 
while i >= 0:
    reverse_nums.append(nums[i])
    i -= 1

print(nums)
print(reverse_nums)
print("reversed!")











