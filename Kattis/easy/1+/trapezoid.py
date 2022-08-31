times = int(input())-1

values = list(map(float, input().split()))
totalArea = 0
for _ in range(times):
    tValues = list(map(float, input().split()))
    totalArea += (tValues[0] - values[0]) * (tValues[1] + values[1]) / 2000
    values = tValues

print(totalArea)