def permu(permList, nameList):
    if len(nameList) == 0: # base (no names from nameList are left)
        print(permList)
        return
    else: # recursive
        for i in range(len(nameList)):
            name = nameList[i]
            remaining_names = nameList[:i] + nameList[i+1:]

            #newPermList = []
            #newPermList.append(name)
            permList.append(name)
            permu(permList, remaining_names)
            permList.pop()

p = []
n = ['Julia', 'Lucas', 'Mia']
permu(p, n)

'''
def scramble(r_letters, s_letters):
    """
    Output every possible permutation of a word.
    Each recursive call moves a letter from
    r_letters (remaining letters) to
    s_letters (scrambled letters)
    """
    if len(r_letters) == 0:
        # Base case: All letters used
        print(s_letters)
    else:
        # Recursive case: For each call to scramble()
        # move a letter from remaining to scrambled
        for i in range(len(r_letters)):
            # The letter at index i will be scrambled
            scramble_letter = r_letters[i]  # <- first letter is being used
            
            # Remove letter to scramble from remaining letters list
            remaining_letters = r_letters[:i] + r_letters[i+1:] # everything before i + everything after i
            
            # Scramble letter
            scramble(remaining_letters, s_letters + scramble_letter) # recur: unused, and add i to used

#word = input("Enter a word to be scrambled: ")
#scramble(word, "")
'''

# main
