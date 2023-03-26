turns = int(input())


def paint(b):
    for row in b:
        if row.count("R") == 8:
            return "R"
        elif row.count("B") == 8:
            return "B"
    for i in range(8):
        temp = ""
        for j in range(8):
            temp += board[j][i]
        if temp == "RRRRRRRR":
            return "R"
        elif temp == "BBBBBBBB":
            return "B"


for turn in range(turns):
    board = []
    for i1 in range(9):
        if i1 == 0:
            row = input()
            pass
        else:
            board.append(input())

    a = paint(board)
    print(a)
