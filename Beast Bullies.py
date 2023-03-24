name1 = input()
name2 = input()

result = ''
while name1 and name2:
    if name1[0] > name2[0]:
        result += name2[0]
        name2 = name2[1:]
    else:
        result += name1[0]
        name1 = name1[1:]
result += (name2 + name1)
print(result)
