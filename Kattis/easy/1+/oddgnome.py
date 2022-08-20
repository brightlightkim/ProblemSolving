times = int(input())

for _ in range(times):
    values = list(map(int, input().split()))
    array = values[1:]
    for i in range(1, len(array)):
        if array[i] != array[i-1]+1:
            print(i+1)
            break