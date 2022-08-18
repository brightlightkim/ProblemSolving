times = int(input())

for _ in range(times):
    values = list(map(int, input().split()))
    worthAdvertise = (values[1] - values[2]) - values[0]
    if worthAdvertise > 0:
        print('advertise')
    elif worthAdvertise == 0:
        print('does not matter')
    else:
        print('do not advertise')