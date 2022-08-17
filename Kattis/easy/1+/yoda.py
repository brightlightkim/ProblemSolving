inputA = list(map(int, input().split()))
inputB = list(map(int, input().split()))

iterating_list = None
other_list = None
starting_point = 0
if len(inputA) > len(inputB):
    iterating_list = inputA.copy()
    other_list = inputB.copy()
    starting_point = len(inputA) - len(inputB)
else:
    iterating_list = inputB.copy()
    other_list = inputA.copy()
    starting_point = len(inputB) - len(inputA)

listA = []
listB = []
pointer = 0
won = True
for i in range(len(iterating_list)):
    if i < starting_point:
        # iterating list has bigger point
        listA.append(str(iterating_list[i]))
    else:
        if iterating_list[i] > other_list[pointer]:
            listA.append(str(iterating_list[i]))
        elif iterating_list[i] == other_list[pointer]:
            listA.append(str(iterating_list[i]))
            won = False
        else:
            listB.append(str(other_list[pointer]))
        pointer += 1

if len(listA) == 0 and won:
    listA = ['0']
elif len(listA) == 0 and not won:
    listA = ['YODA']
if len(listB) == 0 and won:
    listB = ['0']
elif len(listB) == 0 and not won:
    listB = ['YODA']

if iterating_list == inputA:
    print(''.join(map(str, listA)))
    print(''.join(map(str, listB)))
else:
    print(''.join(map(str, listB)))
    print(''.join(map(str, listA)))


