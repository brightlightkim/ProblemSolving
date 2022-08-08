array = list(map(str, input().split(';')))

count = 0
for items in array:
    if len(items) == 1:
        count += 1
    else:
        values = list(map(int, items.split('-')))
        count += values[1] - values[0] + 1
print(count)