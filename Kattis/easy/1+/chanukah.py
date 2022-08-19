times = int(input())

for time in range(times):
    inputs = list(map(int, input().split()))
    total = 0
    for i in range(inputs[1]):
        total += (i+1)
    total+= inputs[1]
    print(time+1, total)