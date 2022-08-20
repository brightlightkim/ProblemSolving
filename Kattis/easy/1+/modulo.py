total = 0

values = {}
for _ in range(10):
    value = int(input())
    if (value % 42) not in values:
        values[value % 42] = 1

print(len(values))