vMap = {}
total = 0
correct = 0
values = ['1']
while values[0] != '-1':
    values = list(map(str, input().split()))
    if values[0] == '-1':
        break
    if values[2] == 'right':
        correct += 1
        if values[1] in vMap:
            total += int(values[0]) + vMap[values[1]]
        else:
            total += int(values[0])
    else:
        if values[1] in vMap:
            vMap[values[1]] += 20
        else:
            vMap[values[1]] = 20
print(correct, total)