import math
times = int(input())

total = 0

for _ in range(times):
    string = input()
    total += math.pow(int(string[:-1]), int(string[len(string)-1]))

print(int(total))
