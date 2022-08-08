dogs = list(map(int, input().split()))
mens = list(map(int, input().split()))

for i in range(len(mens)):
    firstVal = mens[i] % (dogs[0] + dogs[1])
    secondVal = mens[i] % (dogs[2] + dogs[3])
    isFirst = False
    isSecond = False
    if firstVal <= dogs[0] and firstVal != 0:
        isFirst = True
    if secondVal <= dogs[2] and secondVal != 0:
        isSecond = True
    if isFirst and isSecond:
        print('both')
    elif isFirst or isSecond:
        print('one')
    else:
        print('none')

