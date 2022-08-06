import math
times = int(input())

for num in range(times):
    val = int(input())
    if val < 400:
        print(1)
    else:
        print(int(math.ceil(val / 400)))