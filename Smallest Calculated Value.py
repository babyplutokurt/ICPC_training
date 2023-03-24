a = [int(a) for a in input().split()]
num1 = a[0]
num2 = a[1]
num3 = a[2]

ops = []
ops2 = []
for i in range(4):
    if i == 0:
        a = num1 + num2
        ops.append(a)
    elif i == 1:
        a = num1 - num2
        ops.append(a)
    elif i == 2:
        a = num1 * num2
        ops.append(a)
    else:
        if num1 % num2 == 0:
            a = num1 // num2
            ops.append(a)
        else:
            ops.append("Jump")

for op in ops:
    if op != "Jump":
        for j in range(4):

            if j == 0:
                a = op + num3
                # print("Check: ", a)

            elif j == 1:
                a = op - num3

            elif j == 2:
                a = op * num3

            else:
                if op % num3 == 0:
                    a = op // num3
            if a >= 0:
                ops2.append(a)

print(min(ops2))
