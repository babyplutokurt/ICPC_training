def hasPath(maze, start, destination) -> bool:
    row = len(maze)
    col = len(maze[0])

    for r in range(row):
        maze[r] = [1] + maze[r] + [1]
    maze = [[1] * (col + 2)] + maze + [[1] * (col + 2)]
    print(maze)

    row += 2
    col += 2
    start[0] += 1
    start[1] += 1
    destination[0] += 1
    destination[1] += 1

    queue = [start]
    visited_queue = set([])
    visited_queue.add((start[0], start[1]))
    visited = set([])
    visited.add((start[0], start[1]))
    while queue:
        curr = queue.pop(0)
        for r1 in range(curr[0], -1, -1):

            if maze[r1 - 1][curr[1]] == 1:
                if (r1, curr[1]) not in visited_queue:
                    queue.append([r1, curr[1]])
                    visited_queue.add((r1, curr[1]))
                    visited.add((r1, curr[1]))
                break
            visited.add((r1, curr[1]))

        for r2 in range(curr[0], row, 1):
            print(r2 + 1, curr[1])
            print(maze[r2 + 1][curr[1]])
            if maze[r2 + 1][curr[1]] == 1:
                if (r2, curr[1]) not in visited_queue:
                    queue.append([r2, curr[1]])
                    visited_queue.add((r2, curr[1]))
                    visited.add((r2, curr[1]))
                break
            visited.add((r2, curr[1]))

        for c1 in range(curr[1], -1, -1):
            if maze[curr[0]][c1 - 1] == 1:
                if (curr[0], c1) not in visited_queue:
                    queue.append([curr[0], c1])
                    visited_queue.add((curr[0], c1))
                    visited.add((curr[0], c1))
                break
            visited.add((curr[0], c1))

        for c2 in range(curr[1], col, 1):
            if maze[curr[0]][c2 + 1] == 1:
                if (curr[0], c2) not in visited_queue:
                    queue.append([curr[0], c2])
                    visited_queue.add((curr[0], c2))
                    visited.add((curr[0], c2))
                break
            visited.add((curr[0], c2))

    return (destination[0], destination[1]) in visited_queue


a = [[0, 0, 0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 0]]

print(hasPath(a, [0, 0], [8, 6]))
