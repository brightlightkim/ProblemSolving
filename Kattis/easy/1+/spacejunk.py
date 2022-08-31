times = int(input())
values = list(map(int, input().split()))
minJunkDateIndex = [values[0], 0]
for i in range(times):
    if values[i] < minJunkDateIndex[0]:
        minJunkDateIndex = [values[i], i]

print(minJunkDateIndex[1])