fruits = list(map(float, input().split()))

ratios = list(map(float, input().split()))

divVal = 1000
for i in range(3):
    thisDiv = fruits[i]/ratios[i]
    if thisDiv < divVal:
        divVal = thisDiv

for i in range(3):
    leftover = fruits[i] - divVal * ratios[i]
    print("%0.6f" % leftover, end=' ')