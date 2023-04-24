n, k = map(int, input().split())
st = input()
a, b, d, ans = 0, 0, 0, 0
for i in range(n):
    if st[i] == 'a':
        a += 1
    else:
        b += 1
    if a <= k or b <= k:
        ans = max(ans, i + 1 - d)
    else:
        if st[d] == 'a':
            a -= 1
        else:
            b -= 1
        d += 1
print(ans)
