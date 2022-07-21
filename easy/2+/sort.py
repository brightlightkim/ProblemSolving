from collections import Counter
n, c = map(int, input().split())
nums = list(map(int, input().split()))
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
    while count > 2:
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

# while True:
#     max_val = max(dict.values())
#     pop_list = []
#     for key, value in dict.items():
#         if value == max_val:
#             pop_list.append(key)
#             for j in range(value):
#                 print(key, end=' ')
#     for k in range(len(pop_list)):
#         dict.pop(pop_list[k])
#     if not dict:
#         break
