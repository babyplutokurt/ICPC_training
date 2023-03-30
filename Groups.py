turn = int(input())
for t in range(turn):
    n = int(input())
    students = []
    for i in range(n):
        students.append([int(j) for j in input().split()])
    dic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    for day in range(5):
        dic[day] = sum([students[s][day] for s in range(n)])
    print(dic)