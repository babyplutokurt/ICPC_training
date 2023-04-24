def diff(s1, s2):
    res = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            res += 1
    return res
[0, 0, 0, 0, 0]
[1, 1, 1, 1, 1]
for i in range(int(input())):
    s = input()
    if len(s) < 3:
        print(0)
    else:
        s = [int(i) for i in s]
        zeros = [0] + [0] * len(s)
        ones = [0] * len(s) + [0]
        for i in range(1, len(s) + 1):
            zeros[i] = zeros[i - 1] + (1 - s[i - 1])
        for j in range(len(s) - 1, -1, -1):
            ones[j] = ones[j + 1] + s[j]
            if s[j]:
                ones[j] -= 1
        zeros = zeros[1:]
        ones = ones[:-1]
        print(zeros)
        print(ones)
        result = len(s)
        for i in range(len(ones)):
            # 000111
            con1 = (i + 1) - zeros[i] + (len(s) - i - 1 - ones[i])
            con2 = zeros[i] + ones[i]
            result = min(result, con1, con2)
        print(result)
