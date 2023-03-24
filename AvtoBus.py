turn = int(input())
for t in range(turn):
    w = int(input())
    if w % 2 != 0 or w < 4:
        print(-1)
    else:
        if not w % 6:
            min_w = w // 6
        else:
            min_w = w // 6 + 1

        max_w = w // 4

        print(min_w, max_w)