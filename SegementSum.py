a = [int(a) for a in input().split()]
start = a[0]
end = a[1]
diff = a[2]
if diff >= len(str(end)):
    print((end + start) * (end - start + 1) // 2)
else:
    nums = []
    for i in range(start, end):

        if len(set(str(i))) <= diff:
            nums.append(i)
    print(sum(nums) % 998244353)

