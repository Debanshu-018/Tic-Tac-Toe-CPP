# Q1.Rat in a Maze
def rat_in_maze(maze):

    n = len(maze)
    solution = [[0] * n for _ in range(n)]

    def is_safe(row, col):
        return (
            0 <= row < n and
            0 <= col < n and
            maze[row][col] == 1 and
            solution[row][col] == 0
        )

    def solve(row, col):

        if row == n - 1 and col == n - 1:
            solution[row][col] = 1
            return True

        if is_safe(row, col):

            solution[row][col] = 1

            # Down
            if solve(row + 1, col):
                return True

            # Right
            if solve(row, col + 1):
                return True

            # Up
            if solve(row - 1, col):
                return True

            # Left
            if solve(row, col - 1):
                return True

            # Backtrack
            solution[row][col] = 0

        return False

    if solve(0, 0):
        return solution

    return None


maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

result = rat_in_maze(maze)

if result:
    for row in result:
        print(row)
else:
    print("No path found")
