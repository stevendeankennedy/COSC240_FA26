'''
    Converting to binary

    Authors:
        Bailey, Jackson, Declan, Cole
'''

'''
As long as x is greater than 0
   Output x % 2 (remainder is either 0 or 1)
   x = x // 2
'''

# Makes a binary value of an int (in reverse as a string)
def int_to_reverse_binary(integer_value):
    rev_bin = ""
    
    while integer_value > 0:
        b = integer_value % 2
        integer_value = integer_value // 2

        #print(integer_value, b, "?")
        rev_bin += str(b)
        #print(rev_bin)
    return rev_bin

# Return the reverse of a string
def string_reverse(input_string):
    l = len(input_string) - 1
    binary_string = ""

    for i in range(len(input_string)):
        binary_string += input_string[l]
        l -= 1
    return binary_string

    '''
    for letter in input_string
        new_bin = letter + new_bin
    '''
    

# This is for our testing...



'''
    42 / 2 = 21 r 0
    21 / 2 = 10 r 1
    10 / 2 =  5 r 0
     5 / 2 =  2 r 1
     2 / 2 =  1 r 0
     1 / 2 =  0 r 1
'''

if __name__ == "__main__":
    dec_num = 42
    num_rev = int_to_reverse_binary(42)
    bin_num = string_reverse(num_rev)

    print(f"'{dec_num}' ->> '{bin_num}'")
