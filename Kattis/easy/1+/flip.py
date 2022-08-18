values = list(map(str, input().split()))

valA = values[0][2] + values[0][1] + values[0][0]
valB = values[1][2] + values[1][1] + values[1][0]

if int(valA) > int(valB):
    print(valA)
else:
    print(valB)