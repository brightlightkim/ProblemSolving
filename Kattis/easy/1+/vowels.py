string = input()

count = 0
for char in string:
    if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
        count += 1

print(count)