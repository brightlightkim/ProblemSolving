weights = list(map(int, input().split()))

maxWeight = int((weights[0] - weights[1]) * 0.9)

items = list(map(int, input().split()))

totalItemWeight = 0
for item in items:
    totalItemWeight += item

print(maxWeight - totalItemWeight)