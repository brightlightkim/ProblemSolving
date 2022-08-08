string = list(str(input()))
left = 0
right = len(string) - 1
while (left < right):
    string[left], string[right] = string[right], string[left]
    left += 1
    right -= 1

print(''.join(string))