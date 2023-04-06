def rainbow(str):
    dic = {"R": 0, "O": 1, "Y": 2, "G": 3, "B": 4, "I": 5, "V": 6}
    res = [0] * 7
    for s in str:
        res[dic[s]] += 1

    return min(res)


a = "RROOYYYYGGGBBIIIIIIIIBVVVV"
print(rainbow(a))