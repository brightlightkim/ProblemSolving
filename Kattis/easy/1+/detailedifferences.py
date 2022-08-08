times = int(input())

for _ in range(times):
    stringA = input()
    stringB = input()
    print(stringA)
    print(stringB)
    for i in range(len(stringA)):
        if stringA[i] == stringB[i]:
            print('.', end='')
        else:
            print('*', end='')
    print('\n')
