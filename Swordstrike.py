num = int(input())
dic_x = {}
dic_y = {}


def sword(dic_x, dic_y):
    dic_x_max = max(dic_x, key=lambda x: sum(item['v'] for item in dic_x[x]))
    dic_y_max = max(dic_y, key=lambda x: sum(item['v'] for item in dic_y[x]))
    if sum(item['v'] for item in dic_x[dic_x_max]) > sum(item['v'] for item in dic_y[dic_y_max]):
        reward = sum(item['v'] for item in dic_x[dic_x_max])
        for monster in dic_x[dic_x_max]:
            dic_y[monster['y']].remove({'x': dic_x_max, 'v': monster['v']})
        del dic_x[dic_x_max]
    else:
        reward = sum(item['v'] for item in dic_y[dic_y_max])
        for monster in dic_y[dic_y_max]:
            dic_x[monster['x']].remove({'y': dic_y_max, 'v': monster['v']})
        del dic_y[dic_y_max]
    return reward


for i in range(num):
    mon = [int(i) for i in input().split()]
    if mon[0] not in dic_x:
        dic_x[mon[0]] = [{'y': mon[1], 'v': mon[2]}]
    else:
        dic_x[mon[0]].append({'y': mon[1], 'v': mon[2]})
    if mon[1] not in dic_y:
        dic_y[mon[1]] = [{'x': mon[0], 'v': mon[2]}]
    else:
        dic_y[mon[1]].append({'x': mon[0], 'v': mon[2]})
    result = 0

for j in range(min(num, 3)):
    result += sword(dic_x, dic_y)
print(result)
