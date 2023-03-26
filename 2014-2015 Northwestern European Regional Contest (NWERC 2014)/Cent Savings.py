n, d = [int(i) for i in input().split()]
items = [int(i) for i in input().split()]
items.append(0)
# dynamic programming
dp = [[float("inf")] * (n + 1) for i in range(d)]
sum_pre = [0]
for i in range(1, n + 2):
    sum_pre.append(items[i - 1] + sum_pre[i - 1])
sum_pre = sum_pre[1:]

def round_price_(val):
    if val % 10 < 5:
        return val // 10 * 10
    else:
        return val // 10 * 10 + 10

for i in range(1, n):
    dp[0][i] = round_price_(sum_pre[i])

for group in range(1, d): # 分成2 ~ d块
    for index in range(group, n): # 更新list
        for pre in range(0, index):
            dp[group][index] = min(dp[group][index], dp[group - 1][pre] + round_price_(sum_pre[index] - sum_pre[pre]))
result = float("inf")
for i in range(d):
    result = min(result, dp[i][-2])

res2 = []
for i in range(1, n):
    if dp[-1][i] < 2 ** 31:
        res2.append(dp[-1][i] + round_price_(sum_pre[-2] - sum_pre[i - 1]))

res = min(res2)
print(min(result, res))