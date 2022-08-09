import math
values = list(map(int, input().split()))

for _ in range(values[0]):
    matchLen = int(input())
    if matchLen <= math.sqrt(values[1]**2 + values[2]**2):
        print('DA')
    else:
        print('NE')

