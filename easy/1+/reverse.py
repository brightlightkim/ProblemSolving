times = int(input())
array = []
for i in range(times):
    array.append(int(input()))

for val in range(len(array)-1, -1, -1):
    print(array[val])