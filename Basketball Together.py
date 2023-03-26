ene_ = [int(i) for i in input().split()]
teams_ = [int(j) for j in input().split()]

n_ = ene_[0]
enemy_ = ene_[1]
teams_.sort()


def com(teams, n, enemy):
    left, right, res = 0, len(teams) - 1, 0
    curr = 0
    count_mem = 0
    while right > left:
        if teams[right] > enemy:
            res += 1
            right -= 1
        else:
            curr = teams[right] + teams[right]
            while curr < enemy:
                if right - left == 1:
                    return res
                else:
                    left += 1
                    curr += teams[right]
            res += 1
            right -= 1
            left += 1
    return res


a = com(teams_, n_, enemy_)
print(a)
