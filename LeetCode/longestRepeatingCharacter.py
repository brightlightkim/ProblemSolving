s = input()
k = int(input())
dict = {}
max = 0
for i in range(len(s)):
    if s[i] in dict:
        dict[s[i]] += 1
    else:
        dict[s[i]] = 1
for num in dict:
    count = dict[num]
    st = 0
    lt = len(s) - 1
    while count >= 2:
        blank = lt - st - 2
        leng = 0
        if blank > k:
            leng = k + 1
        elif blank == k:
            leng = k + 2
        else:
            leng = blank + 2
        if (leng > max):
            max = leng
        count -= 1

print(max)