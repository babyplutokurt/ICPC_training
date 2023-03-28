turn = int(input())
def judge(n, s1, s2):
    for i in range(n):
        if s1[i] == s2[i]:
            pass
        else:
            if s1[i] != "R" and s2[i] != "R":
                pass
            else:
                return "NO"
    return "YES"

for t in range(turn):
    n = int(input())
    s1 = input()
    s2 = input()
    print(judge(n, s1, s2))
