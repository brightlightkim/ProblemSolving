cases = int(input())

for case in range(cases):
    R, C = map(int, input().split())
    table = []
    isTreeInPaint = False
    for r in range(R):
        string = input()
        table.extend(string)
        if '^' in string:
            isTreeInPaint = True
    if R == 1 or C == 1 and isTreeInPaint:
        print('Case #' + str(case+1) + ': Impossible')
    else:
        print('Case #' + str(case + 1) + ': Possible')
        for r in range(R):
            for c in range(C):
                print('^', end='')
            print('')
