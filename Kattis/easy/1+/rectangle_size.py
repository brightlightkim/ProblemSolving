points = list(map(float, input().split()))

width = 0
if points[2] > points[0]:
    width = points[2] - points[0]
else:
    width = points[0] - points[2]
height = 0
if points[3] > points[1]:
    height = points[3] - points[1]
else:
    height = points[1] - points[3]
area = width * height
print("%.3f" % area)