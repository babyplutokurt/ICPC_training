def numIslands(grid) -> int:
    res = 0
    visited = set([])

    def bfs(row, col):
        queue = [(row, col)]
        while queue:
            row, col = queue.pop(0)
            visited.add((row, col))
            neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for i, j in neighbors:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in visited:
                    visited.add((i, j))
                    if grid[i][j] == '1':
                        queue.append((i, j))
        return

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == '1':
                bfs(i, j)
                res += 1
    return res


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(numIslands(grid))
