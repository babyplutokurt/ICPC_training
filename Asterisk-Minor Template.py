turn = int(input())
def f(s1, s2):
    for i in range(len(s1) - 1):
        if s1[i: i + 2] in s2:
            print("YES")
            print("*" + s1[i: i + 2] + "*")
            return
    print("NO")
for t in range(turn):
    s1 = input()
    s2 = input()
    if s1[0] == s2[0]:
        print("YES")
        print(s1[0] + '*')
    elif s1[-1] == s2[-1]:
        print("YES")
        print("*" + s1[-1])
    else:
        f(s1, s2)

