times = int(input())

count = 0
wordMap = {}
for _ in range(times):
    strings = list(map(str, input().split()))

    if strings[0] not in wordMap:
        print(strings[0], strings[1])
        wordMap[strings[0]] = 1
        count+=1
        if count == 12:
            break

