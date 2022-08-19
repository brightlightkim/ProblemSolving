import math
times = int(input())

for _ in range(times):
    values = list(map(float, input().split()))
    v = values[0]
    degree = values[1] / 180 * math.pi
    x1 = values[2]
    h1 = values[3]+1
    h2 = values[4]-1

    t = x1 / (v * math.cos(degree))

    height = v * t * math.sin(degree) - 0.5 * 9.81 * t * t

    if h1 <= height <= h2:
        print('Safe')
    else:
        print('Not Safe')

