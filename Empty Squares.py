lst = [int(i) for i in input().split()]

left = min(lst[2], lst[0] - lst[1] - lst[2])
right = max(lst[2], lst[0] - lst[1] - lst[2])

if lst[1] != left and lst[1] != right:
    if left != right or (right == 0):
        print(0)
    else:
        if left == 1:
            print(1)
        elif left == 2:
            if lst[1] == 1:
                print(2)
            else:
                print(1)
        elif left == 3:
            if lst[1] == 1:
                print(1)
            elif lst[1] == 2:
                print(2)
            else:
                print(0)
        elif left == 4:
            if lst[1] == 1:
                print(1)
            elif lst[1] == 3:
                print(1)
            else:
                print(0)
        else:
            print(0)




elif lst[1] == left and lst[1] == right:
    if lst[1] == 1:
        print(2)
    elif lst[1] == 2:
        print(3)
    elif lst[1] == 3:
        print(3)
    elif lst[1] == 4:
        print(2)
    else:
        print(0)

elif lst[1] == left:
    if left > 2:
        print(0)
    if left <= 2:
        print(1)
elif lst[1] == right:
    if right <= 3:
        if right == 1:
            print(1)
        if right == 2:
            if not left:
                print(1)
            else:
                print(2)
        if right == 3:
            # print("here")
            print(left)
    else:
        if left == 1 or left == right - 1:
            print(1)
        else:
            print(0)




