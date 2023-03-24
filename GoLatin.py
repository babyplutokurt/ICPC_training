Turn = int(input())
dic = {"a": "as", "i": "ios", "y": "ios",
       "l": "les", "n": "anes", "ne": "anes",
       "o": "os", "r": "res", "t": "tas",
       "u": "us", "v": "ves", "w": "was"}
for i in range(Turn):
    word = input()
    if word[-1] not in dic and (word[-2] + word[-1]) not in dic:
        print(word + "us")
    elif (word[-2] + word[-1]) in dic:
        print(word[:-2] + dic[(word[-2] + word[-1])])
    else:
        print(word[:-1] + dic[word[-1]])
