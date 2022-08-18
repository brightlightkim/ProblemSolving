electricity = int(input())
times = int(input())
leftover = 0
for _ in range(times):
    leftover += electricity - int(input())

print(leftover + electricity)