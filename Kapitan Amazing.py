c = 'QWERTYUIOPASDFGHJKLZXCVBNM'
s = ''
for i in range(3):
    s += input()
turn = int(input())
container = set()
for i in range(len(c)):
    if s[i] == "*":
        container.add(c[i])
for t in range(turn):
    pswd = input()
    pw = set(pswd)
    if (pw == container):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")