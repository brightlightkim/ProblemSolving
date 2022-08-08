# values = list(input().split())
# n, k = map(int, values[:2])
n, k, rate = input().split()
n, k, rate = int(n), int(k), float(rate)
if n * rate >= k:
    print("spela inte!")
else:
    print("spela")