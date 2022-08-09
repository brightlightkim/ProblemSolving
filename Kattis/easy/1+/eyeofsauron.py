string = input()

leftIndex = 0
rightIndex = 0
for i in range(len(string)):
    if string[i] == '(':
        leftIndex = i
        rightIndex = i+1
        break

if leftIndex+1 == len(string)/2 :
    print('correct')
else:
    print('fix')