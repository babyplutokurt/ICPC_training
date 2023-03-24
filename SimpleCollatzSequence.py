letterel = input()


def process():
    end = False
    for i in range(7):
        guess = input()
        response = ''
        if not end:
            for j in range(5):
                if guess[j] not in letterel:
                    response += "X"
                elif guess[j] == letterel[j]:
                    response += "G"
                else:
                    response += "Y"
            if response == "GGGGG":
                print("WINNER")
                end = True
            else:
                if i < 6:
                    print(response)
                else:
                    print("LOSER")
        else:
            pass

    return

process()