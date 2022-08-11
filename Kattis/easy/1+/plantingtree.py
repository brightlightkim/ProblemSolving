times = int(input())
seeds = list(map(int, input().split()))

seeds.sort(reverse=True)

maxTime = 0
day = 0
for seed in seeds:
    day += 1
    if seed + day > maxTime:
        maxTime = seed + day
print(maxTime+1)