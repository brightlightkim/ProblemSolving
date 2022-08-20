cases = int(input())

for time in range(cases):
    times = int(input())
    guests = list(map(int, input().split()))
    couples = {}
    for guest in guests:
        if guest not in couples:
            couples[guest] = 1
        else:
            couples[guest] += 1

    for key in couples:
        if couples[key] == 1:
            print('Case #'+ str(time + 1) +': ' + str(key))
            break
