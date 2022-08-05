array = list(map(str, input().split()))

isHere = False
for s1 in range(len(array)):
    for s2 in range(s1+1, len(array)):
        if array[s1] == array[s2]:
            isHere = True
            break

if isHere:
    print("no")
else:
    print("yes")