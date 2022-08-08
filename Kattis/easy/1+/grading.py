grades = list(map(int, input().split()))
A = grades[0]
B = grades[1]
C = grades[2]
D = grades[3]
E = grades[4]

grade = int(input())

if grade >= A:
    print('A')
elif grade >= B:
    print('B')
elif grade >= C:
    print('C')
elif grade >= D:
    print('D')
elif grade >= E:
    print('E')
else:
    print('F')