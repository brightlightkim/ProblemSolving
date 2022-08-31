string = input()

P = []
K = []
H = []
T = []

isGreska = False

for i in range(len(string)):
    word = string[i]
    if word.isalpha():
        number = string[i+1] + string[i+2]
        if word == 'P':
            if number in P:
                isGreska = True
                break
            else:
                P.append(number)
        elif word == 'K':
            if number in K:
                isGreska = True
                break
            else:
                K.append(number)
        elif word == 'H':
            if number in H:
                isGreska = True
                break
            else:
                H.append(number)
        else:
            if number in T:
                isGreska = True
                break
            else:
                T.append(number)

if isGreska:
    print("GRESKA")
else:
    print(13-len(P), 13-len(K), 13-len(H), 13-len(T))



