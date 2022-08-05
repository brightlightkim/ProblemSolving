times = int(input())

for i in range(times):
    numbers = list(map(int, input().split()))
    calculable = False
    if numbers[0]+numbers[1] == numbers[2]:
        calculable = True
    if numbers[0]-numbers[1] == numbers[2] or numbers[1] - numbers[0] == numbers[2]:
        calculable = True
    if numbers[0]*numbers[1] == numbers[2]:
        calculable = True
    if numbers[0]/numbers[1] ==numbers[2] or numbers[1]/numbers[0] == numbers[2]:
        calculable = True

    if calculable:
        print("Possible")
    else:
        print("Impossible")