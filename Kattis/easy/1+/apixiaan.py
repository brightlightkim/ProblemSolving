string = input()

finalString = ''
for char in string:
    if len(finalString) ==0:
        finalString = char
    elif char != finalString[len(finalString)-1]:
        finalString+=char

print(finalString)