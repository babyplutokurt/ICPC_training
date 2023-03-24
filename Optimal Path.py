turn = int(input())
for t in range(turn):
    lst = [int(i) for i in input().split()]
    n = lst[1]
    m = lst[0]

    if m == 1 or n == 1:
        print(((m + n) * (m + n - 1)) // 2)
    else:
        print(n * (n - 1) // 2 + (n + m * n) * m // 2)
"""   
    1 2
    3 4
    5 6
    
    1  2  3  4  5 
    6  7  8  9  10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25
"""