string = input()

index = 0
for i in range(len(string)):
    if string[i] == 'a':
        index = i
        break

print(string[index: len(string)])
