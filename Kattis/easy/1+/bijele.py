chess = list(map(int, input().split()))

king = str(1 - chess[0])
queen = str(1 - chess[1])
rooks = str(2 - chess[2])
bishops = str(2 - chess[3])
knights = str(2 - chess[4])
pawns = str(8 - chess[5])

print(king + ' ' + queen + ' ' + rooks + ' ' + bishops + ' ' + knights + ' '+ pawns)

