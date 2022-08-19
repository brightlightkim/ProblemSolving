times = int(input())

for _ in range(times):
    values = list(map(int, input().split()))

    K = values[0]
    N = values[1]

    sumP = 0
    sumO = 0
    sumE = 0
    # sum of positive
    for num in range(1, N+1):
        sumP+=num
    # sum of odd
    for num in range(1, 2*N+1, 2):
        sumO+=num
    # sum of even
    for num in range(2, 2*N+1, 2):
        sumE+=num

    print(K, sumP, sumO, sumE)