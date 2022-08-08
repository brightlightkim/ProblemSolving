wordsNotModified = list(map(str, input().split()))

vowels = ['a', 'e', 'i', 'o', 'u']
for word in wordsNotModified:
    savedWord = ''
    word_iter = iter(word)
    for ch in word_iter:
        savedWord += ch
        if ch in vowels:
            next(word_iter)
            next(word_iter)
    print(savedWord, end =' ')