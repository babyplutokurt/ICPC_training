n = int(input())
DOMjudge, Kattis = {}, []
for i in range(n):
    a = input()
    if a not in DOMjudge:
        DOMjudge[a] = 1
    else:
        DOMjudge[a] += 1
for i in range(n):
    Kattis.append(input())
result = 0
for res in Kattis:
    if res in DOMjudge and DOMjudge[res] > 0:
        result += 1
        DOMjudge[res] -= 1

print(result)