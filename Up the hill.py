up = int(input())
down = int(input())

n = up + down + 1

left = [n]
n -= 1
right = []
while up:
    left.append(n)
    n -= 1
    up -= 1
left = left[::-1]
while down:
    left.append(n)
    n -= 1
    down -= 1
print(" ".join([str(i) for i in left]))