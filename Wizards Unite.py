Turn = int(input())
for i in range(Turn):
    chest_key = [int(x) for x in input().split(" ")]
    times = [int(x) for x in input().split(" ")]
    chests = chest_key[0]
    silver = chest_key[1]
    if silver == 0:
        print(sum(times))
    else:
        times.sort()
        max_silver = times[-1]
        print(max(sum(times[0: -silver]), max_silver))
