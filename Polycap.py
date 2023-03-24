turns = int(input())
for turn in range(turns):
    n = int(input())
    s = [i for i in input().split()]
    s2 = set(s)
    while len(s) != len(s2):
        s = s[len(s) - (len(s2)):]
        s2 = set(s)
    print(n - len(s2))
