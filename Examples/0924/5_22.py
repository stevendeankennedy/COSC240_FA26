'''
    Lab 5.22 - ish
'''

#ex CRASH v CRUSH outputs 4

word1 = "zebra"
word2 = "zobryaaaaaaa"

count = 0 # num of matching letters
for i in range(min(len(word1), len(word2))):
    print(i, word1[i], word2[i])
    if word1[i] == word2[i]:
        count += 1

print("count:", count)
