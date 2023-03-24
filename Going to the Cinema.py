Turn = int(input())
for i in range(Turn):
    nums = int(input())
    reqs = [int(x) for x in input().split(" ")]
    reqs.sort()
    count = 0
    ind = 0
    if reqs[0] != 0:
        count += 1

    for index in range(nums - 1):
        if reqs[index] <= index < nums - 1 and reqs[index + 1] > index + 1:
            count += 1
    if reqs[nums - 1] <= nums - 1:
        count += 1

    print(count)

"""
    if reqs[0] != 0:
        count += 1
    for index in range(ind, nums):
        satisfy = True
        if index == reqs[index] and index < nums - 1 and reqs[index + 1] > index + 1:
            count += 1
        else:
            # print("index: ", index)
            for person in range(ind, index + 1):
                # index = 去其他的人数
                if reqs[person] > index:
                    satisfy = False
                    break
            for person in range(index + 1, nums):
                if reqs[person] <= index + 1:
                    satisfy = False
                    break
            if satisfy:
                count += 1
        ind = index
"""
