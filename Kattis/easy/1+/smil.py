string = input()

index = 0
stack = []
counts = []
for index in range(len(string)):
    if string[index] == ')':
        if index > 0 and (string[index-1] == ':' or string[index-1] == ';'):
            counts.append(index-1)
        elif index > 1 and ((string[index-2] == ':' or string[index-2] == ';') and string[index-1] == '-'):
            counts.append(index-2)

for num in counts:
    print(num)


