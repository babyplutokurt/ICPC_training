Turn = int(input())
for turn in range(Turn):
    s = input()
    if len(s) <= 2:
        print(0)
    else:
        one = s.count("1")
        zero = s.count("0")
        if one == zero:
            print(one - 1)
        else:
            print(min(one, zero))