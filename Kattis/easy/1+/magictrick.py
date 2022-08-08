from collections import Counter
string = input()
map = Counter(list(string))
valid = 1
for i in map:
    if map[i] > 1:
        valid = 0
        break
print(valid)

