lst = [int(i) for i in input().split()]

for j in range(lst[0]):
    temp = [w for w in input().split()]
    res = ""
    if temp[0] == "Y":
        res += "Y"
        lst[1] -= 1
        lst[2] += 1
    elif temp[0] == "N":
        if not lst[2]:
            res += "Y"
            lst[1] -= 1
            lst[2] += 1
        else:
            res += "N"

    if temp[1] == "Y":
        res += "Y"
        lst[2] -= 1
        lst[1] += 1
    elif temp[1] == "N":
        if not lst[1]:
            res += "Y"
            lst[2] -= 1
            lst[1] += 1
        else:
            res += "N"

    print(res[0] + " " + res[1])


