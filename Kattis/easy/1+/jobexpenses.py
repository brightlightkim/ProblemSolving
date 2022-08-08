times = int(input())
array = list(map(int, input().split()))
sum = 0
for i in range(times):
    if array[i] < 0:
        sum+=abs(array[i])
print(sum)