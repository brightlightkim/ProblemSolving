caseNum = int(input())

for case in range(caseNum):
    N, K = map(int, input().split())
    values = list(map(int, input().split()))
    if K*2 < len(values):
        print("Case #" + str(case+1) + ": NO")
    else:
        vDict = {}
        isTrue = True
        for value in values:
            if value in vDict:
                vDict[value] += 1
            else:
                vDict[value] = 1
            if vDict[value] > 2:
                print("Case #" + str(case + 1) + ": NO")
                isTrue = False
                break
        if isTrue:
            print("Case #" + str(case + 1) + ": YES")

