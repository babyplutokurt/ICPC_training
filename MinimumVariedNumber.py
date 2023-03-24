turn = int(input())
for t in range(turn):
    s = int(input())
    if s < 10:
        print(s)
    else:
        last = 9
        result = ''
        while s >= last + 1:
            s -= last
            result = str(last) + result
            last -= 1
        if s:
            result = str(s) + result
            print(result)
        else:
            print(result)