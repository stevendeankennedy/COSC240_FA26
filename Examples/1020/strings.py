'''
    SSSTTTTRRRINNGSSSS Examples

    Special Thanks:
        Bailey
'''

# slicing
example = "Bailey's favorite holiday is Christmas"

print(example)
print(example[0])
print(example[0:5]) # slicing, gets substrings
print(example[3:9])
print(example[6:-5])
print(example[:-5])
print(example[::2]) # BEGIN, END, STRIDE*

example = "The quick brown fox jumped over the box"

x = example.find("h")
print(x)

tokens = example.split()
print(example)
print(tokens)

example = "a,b,c,d"
tokens = example.split(',') # use comma delimiter
print(example)
print(tokens)

separator = "/"
example = separator.join(tokens)
print(example)

example = '/'.join(tokens)
print(example)
