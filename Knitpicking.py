n = int(input())
dic = {}
loc = {'any': 0, "left": 1, "right": 2}
res = 0
res_max = 0
for i in range(n):
    sock = [i for i in input().split()]
    res += int(sock[2])
    if sock[0] not in dic:
        dic[sock[0]] = [0, 0, 0]
        dic[sock[0]][loc[sock[1]]] = int(sock[2])
    else:
        dic[sock[0]][loc[sock[1]]] = int(sock[2])

any_ = False
for j in dic:
    if not any_ and dic[j][0] and (dic[j][1] or dic[j][2]):
        any_ = True
        res_max += (1 + max(dic[j][1], dic[j][2]))
    elif dic[j][0] and not (dic[j][1] or dic[j][2]):
        res_max += 1
    else:
        res_max += max(dic[j][1], dic[j][2])
if res_max >= res:
    print("impossible")
elif not any_:
    print(res_max + 1)
else:
    print(res_max)