Turn = int(input())


def remove(s, length):
    count = 1
    pointer = s[0]
    for c in range(length):
        if s[c] != pointer:
            count += 1
            pointer = s[c]
    if s[0] == s[-1]:
        return (count + 1) // 2
    else:
        return (count + 1) // 2 + 1


for i in range(Turn):
    reqs = [int(x) for x in input().split(" ")]
    n = reqs[0]
    a = reqs[1]
    b = reqs[2]
    num = input()
    if b > 0:
        print(n * a + n * b)
    else:
        count = remove(num, n)
        print(n * a + count * b)
