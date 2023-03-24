turns = int(input())
for turn in range(turns):
    board = []
    for i in range(9):
        if i == 0:
            row = input()
            pass
        else:
            board.append([])
            row = input()
            for j in row:
                board[i - 1].append(j)
    for r in board:
        if r.count("R") == 8:
            print("R")
        elif r.count("B") == 8:
            print("B")
    res = 0
    for col in range(8):
        init = board[0][col]
        if init == ".":
            pass
        else:
            for r2 in range(1, 8):
                if board[r2][col] != init:
                    break
                if res < 1 and r2 == 7:
                    print(init)
                    res += 1

