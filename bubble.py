turn = int(input())
for t in range(turn):
    light_string = input()
    lst = [i for i in light_string]
    s = set(lst)
    if len(s) == 1:
        print(-1)
    else:
        if len(s) >= 3:
            print(4)
        elif len(s) == 2:
            a = s.pop()
            if light_string.count(a) == 2:
                print(4)
            else:
                print(6)
        else:
            print(-1)


