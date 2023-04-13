import math

turn = int(input())
for t in range(turn):
    lst = [int(i) for i in input().split()]
    if math.gcd(lst[0], lst[1]) == 1:
        print(1)
        print(*lst)
    else:
        i = 1
        if lst[0] < 5 * 10e7 and lst[1] < 5 * 10e7:
            while math.gcd(lst[0] + 1, lst[1] + i) != 1 and lst[0] + 1 <= 10e9 and lst[1] + i <= 10e9:
                i += 1
            print(2)
            print(lst[0] + 1, lst[1] + i)
            print(*lst)
        elif lst[0] > 5 * 10e7 > lst[1]:
            while math.gcd(lst[0] - 1, lst[1] + i) != 1 and lst[0] + 1 <= 10e9 and lst[1] + i <= 10e9:
                i += 1
            print(2)
            print(lst[0] - 1, lst[1] + i)
            print(*lst)
        elif lst[0] > 5 * 10e7 and lst[1] > 5 * 10e7:

            while math.gcd(lst[0] - 1, lst[1] - i) != 1 and lst[0] + 1 <= 10e9 and lst[1] - i <= 10e9:
                i -= 1
            print(2)
            print(lst[0] - 1, lst[1] - i)
            print(*lst)
        else:
            while math.gcd(lst[0] + 1, lst[1] - i) != 1 and lst[0] + 1 <= 10e9 and lst[1] - i <= 10e9:
                i -= 1
            print(2)
            print(lst[0] + 1, lst[1] - i)
            print(*lst)
