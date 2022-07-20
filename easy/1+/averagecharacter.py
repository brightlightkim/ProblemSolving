import math
s = input()
sum = 0
for i in range(len(s)):
    sum += ord(s[i])
average = sum / len(s)
print(chr(math.floor(average)))