from collections import Counter
n, c = map(int, input().split())
nums = list(map(int, input().split()))
dict = {}
for i in range(len(nums)):
    if nums[i] in dict:
        dict[nums[i]] += 1
    else:
        dict[nums[i]] = 1
indexMap = {}
for num in dict:
    if dict[num] in indexMap:
        indexMap[dict[num]].append(num)
    else:
        indexMap[dict[num]] = [num]

for freq in sorted(indexMap, reverse=True):
    for num in indexMap[freq]:
        for _ in range(freq):
            print(num, end=' ')

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
