'''
    ¿qué es?  RUN-LENGTH ENCODING, amigos!

    Authors: Declan, Dusty, Bailey, Michael R, and friends
'''

# take an input string and compress it with our
#   run-length encoding algo
def compress(text):
    output = ''
    current = text[0] # start with the first letter
    count = 1

    # iterate through input text
    for i in range(1, len(text)):
        # check current letter
        #print(text[i])
        # is it the same letter?
        if (current == text[i]):
            # if it is, then add 1 to a counter
            count = count + 1
        else:
            print(current, '->', count)
            output += f"{current} {count},"
            current = text[i]
            count = 1

    print(current, '->', count)
    output += f"{current} {count}"
    return output

# Reverse the compression algo
def decompress(text):
    output = ''
    letters = text.split(',')
    print(letters)
    for i in range(len(letters)):
        pair = letters[i].split()
        for j in range(int(pair[1])):
            output += pair[0]

    return output

def show_it_working(text):
    result = compress(text)
    print(f"input:{text}\noutput:{result}")
    result1 = decompress(result)
    print("Decompressed:", result1)
    if (text == result1):
        print("yay!")
    else:
        print("nay!")

show_it_working("aaaaaabbbbbcccccccccddddefffffffff")













