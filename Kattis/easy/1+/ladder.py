import math
h, degree = map(int, input().split())

theta = degree * math.pi / 180

height = math.ceil(h / math.sin(theta))

print(height)