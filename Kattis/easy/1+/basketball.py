string = input()

A = 0
B = 0
for i in range(0, len(string), 2):
    if string[i] == 'A':
        A += int(string[i+1])
    else:
        B += int(string[i+1])

    if (A > B + 1 and A > 10) or ((A > 9 and B > 9) and A > B + 1):
        print('A')
        break
    elif (B > A + 1 and B > 10) or ((A > 9 and B > 9) and B > A + 1):
        print('B')
        break