s1, s2 = input().split()

lastWord = s1[len(s1)-1]
if lastWord == 'a' or lastWord =='e' or lastWord=='o' or lastWord=='u' or lastWord=='i':
    if lastWord == 'e':
        print(s1 + 'x' + s2)
    else:
        print(s1[:len(s1)-1] + 'ex' + s2)
else:
    if lastWord == 'x' and s1[len(s1)-2]=='e':
        print(s1 + s2)
    else:
        print(s1 + 'ex' + s2)