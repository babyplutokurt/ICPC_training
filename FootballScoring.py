team1 = [int(i) for i in input().split()]
team2 = [int(i) for i in input().split()]
score = [6, 3, 2, 1, 2]
score1 = sum([team1[j] * score[j] for j in range(5)])
score2 = sum([team2[j] * score[j] for j in range(5)])
print(score1, "  ", score2)