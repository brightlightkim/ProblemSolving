times = input()

values = list(map(int, input().split()))

count = 0
total = 0
for num in values:
    if num != -1:
        total += num
        count += 1

print(total / count)