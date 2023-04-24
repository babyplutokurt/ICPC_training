from math import sqrt

for i in range(int(input())):
    n = int(input())
    factors = []
    for i in range(2, int(sqrt(n) // 1) + 1):
        if i == sqrt(n) // 1 + 1 and n % i:
            factors.append(-1)
        if n % i == 0:
            factors.append(i)
            n = n // i
    for i in range(2, int(sqrt(n) // 1) + 1):
        if i == sqrt(n) // 1 + 1:
            if n % i:
                factors.append(-1)
            else:
                if i in factors:
                    factors.append(-1)
        if n % i == 0 and i not in factors:
            factors.append(i)
            n = n // i
    for i in range(2, int(sqrt(n) // 1) + 1):
        if i == sqrt(n) // 1 + 1:
            if n % i:
                factors.append(-1)
            else:
                if i in factors:
                    factors.append(-1)
        if n % i == 0 and i not in factors:
            factors.append(i)
            n = n // i
    if -1 in factors:
        print("NO")
    else:
        print(*factors)
