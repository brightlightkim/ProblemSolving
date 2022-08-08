dogs = list(map(int, input().split()))
mens = list(map(int, input().split()))

for i in range(len(mens)):
    if mens[i] <= dogs[0] and mens[i] <= dogs[2]:
        print('both')
    elif mens[i] <= dogs[0] or mens[i] <= dogs[2]:
        print('one')
    else:
        print('none')