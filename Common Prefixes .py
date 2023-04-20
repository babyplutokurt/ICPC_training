for i in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    res = ["a" * (max(a) + 1)]
    dic = {"a": "b", "b": "a"}
    for i in a:
        con = res[-1][0:i]
        for j in range(i, max(a) + 1):
            con += dic[res[-1][j]]
        res.append(con)
    for i in res:
        print(i)
