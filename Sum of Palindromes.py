Turn = int(input())


def find_max_pal(num):
    num = str(num)
    if not len(num) % 2:
        a = num[0:len(num) // 2] + num[0:len(num) // 2][::-1]
    else:
        a = num[0:len(num) // 2] + num[0:len(num) // 2 + 1][::-1]
    num_1 = int(a)
    insert = 0
    while num_1 > int(num):
        a = list(a)
        if insert == 0:
            if len(num) % 2 == 0:
                temp = int(a[len(num) // 2 - 1]) - 1
                if temp < 0:
                    temp = 9
                a[len(num) // 2 - 1] = str(temp)
                a[len(num) // 2] = str(temp)
            else:
                temp = int(a[len(num) // 2]) - 1
                if temp < 0:
                    temp = 9
                a[len(num) // 2] = str(temp)
        else:
            if len(num) % 2:
                temp = int(a[len(num) // 2 + insert]) - 1
                if temp < 0:
                    temp = 9
                a[len(num) // 2 + insert] = str(temp)
                a[len(num) // 2 - insert] = str(temp)
                for n in a[len(num) // 2 - insert + 1: len(num) // 2 + insert]:
                    n = "9"
            else:
                temp = int(a[len(num) // 2 - 1 - insert]) - 1
                if temp < 0:
                    temp = 9
                a[len(num) // 2 + insert] = str(temp)
                a[len(num) // 2 - 1 - insert] = str(temp)
                for n in a[len(num) // 2 - insert: len(num) // 2 + insert]:
                    n = "9"
        a = ''.join(a)
        num_1 = int(a)
        insert += 1
    return num_1


for i in range(Turn):
    sum_number = int(input())

    res = []
    while sum_number:
        res += [find_max_pal(sum_number)]
        sum_number -= res[-1]

    print(len(res))
    for result in res:
        print(result)
