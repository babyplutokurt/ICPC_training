lst = [int(i) for i in input().split()]
factor = lst[1] / lst[0]

def game(f):
    res = 0
    if not f.is_integer():
        print(-1)
        return
    else:
        while f != 1:
            #print("X")
            if (f / 3).is_integer():
                res += 1
                f = f / 3
            elif (f / 2).is_integer():
                res += 1
                f = f / 2
            else:
                print(-1)
                return
        print(res)
        return

game(factor)