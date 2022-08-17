values = list(map(int, input().split()))

values.sort()
order = input()

for val in order:
    if val == 'A':
        print(values[0], end= ' ')
    elif val == 'B':
        print(values[1], end= ' ')
    else:
        print(values[2], end= ' ')