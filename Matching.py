for i in range(int(input())):
    a = input()
    if '?' not in a:
        if a[0] == '0':
            print(0)
        else:
            print(1)
    else:
        if a[0] == '0':
            print(0)
        else:
            if a[0] == '?':
                print(9 * (10 ** a[1:].count('?')))
            else:
                print(10 ** a.count('?'))