for i in range(int(input())):
    n = int(input())
    nums = [int(i) for i in input().split()]
    ev, od = 0, 0
    for num in nums:
        if num % 2:
            od += num
        else:
            ev += num
    if ev > od:
        print("YES")
    else:
        print("NO")