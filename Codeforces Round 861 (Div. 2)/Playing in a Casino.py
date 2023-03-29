turn = int(input())
for t in range(turn):
    nums = [int(i) for i in input().split()]
    cards = []
    for i in range(nums[0]):
        cards.append([int(i) for i in input().split()])
    res = 0
    for card in range(len(cards)):
        for index in range(card + 1, len(cards), 1):
            res += sum([abs(cards[card][i] - cards[index][i]) for i in range(nums[1])])

    print(res)

