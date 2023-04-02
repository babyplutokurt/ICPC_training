turn = int(input())
for t in range(turn):
    s = ['0'] * 9
    for i in range(9):
        s[i] = input()
    i = 0
    j = 0
    while i < 3:
        if s[i][j] == '1':
            s[i] = s[i][:j] + '2' + s[i][j+1:]
        else:
            s[i] = s[i][:j] + '1' + s[i][j+1:]
        i += 1
        j += 3
    i = 3
    j = 1
    while i < 6:
        if s[i][j] == '1':
           s[i] = s[i][:j] + '2' + s[i][j+1:]
        else:
            s[i] = s[i][:j] + '1' + s[i][j+1:]
        i += 1
        j += 3
    i = 6
    j = 2
    while i < 9:
        if s[i][j] == '1':
           s[i] = s[i][:j] + '2' + s[i][j+1:]
        else:
           s[i] = s[i][:j] + '1' + s[i][j+1:]
        i += 1
        j += 3
    for i in range(0, 9):
        print(s[i])