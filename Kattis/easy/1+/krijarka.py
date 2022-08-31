word1, word2 = input().split()
word1_index = 0
word2_index = 0
for letter in word1:
    if letter in word2:
        word1_index = word1.index(letter)
        word2_index = word2.index(letter)
        break
i = 0
while i < len(word2):
    j = 0
    while j < len(word1):
        if i == word2_index:
            print(word1, end='')
            j = len(word1)
        elif j == word1_index:
            print(word2[i], end='')
        else:
            print('.', end='')
        j += 1
    i += 1
    print()