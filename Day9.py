#Q1.Trapping Rain Water
def trap(height):
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water

#Q2.Sliding Window Maximum
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):

        # Remove elements outside the window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        # Start adding answers after first window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(max_sliding_window(nums, k))

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print("Trapped Water:", trap(height))

# Q3.Median of Two Sorted Arrays
def find_median(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()

    n = len(nums)

    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2


nums1 = [1, 3]
nums2 = [2]

print("Median:", find_median(nums1, nums2))

#Q4.N-Queens
def solve_n_queens(n):
    board = [["."] * n for _ in range(n)]
    solutions = []

    cols = set()
    diagonals1 = set()
    diagonals2 = set()

    def backtrack(row):
        if row == n:
            solution = ["".join(row) for row in board]
            solutions.append(solution)
            return

        for col in range(n):

            if col in cols:
                continue

            if row - col in diagonals1:
                continue

            if row + col in diagonals2:
                continue

            # Place queen
            board[row][col] = "Q"
            cols.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)

            backtrack(row + 1)

            # Remove queen
            board[row][col] = "."
            cols.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)

    backtrack(0)

    return solutions


n = 4

solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()
    
#OUTPUT
# .Q..
# ...Q
# Q...
# ..Q.

# ..Q.
# Q...
# ...Q
# .Q..
#Q5. Sudoku Solver
def solve_sudoku(board):

    def is_valid(row, col, num):

        # Check row
        for i in range(9):
            if board[row][i] == num:
                return False

        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check 3x3 box
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def solve():

        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":

                    for num in "123456789":

                        if is_valid(row, col, num):

                            board[row][col] = num

                            if solve():
                                return True

                            board[row][col] = "."

                    return False

        return True

    solve()


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solve_sudoku(board)

for row in board:
    print(row)

#Q6. Word Search
def exist(board, word):

    rows = len(board)
    cols = len(board[0])

    def dfs(row, col, index):

        if index == len(word):
            return True

        if (row < 0 or row >= rows or
            col < 0 or col >= cols or
            board[row][col] != word[index]):
            return False

        # Mark as visited
        temp = board[row][col]
        board[row][col] = "#"

        found = (
            dfs(row + 1, col, index + 1) or
            dfs(row - 1, col, index + 1) or
            dfs(row, col + 1, index + 1) or
            dfs(row, col - 1, index + 1)
        )

        # Restore cell
        board[row][col] = temp

        return found

    for row in range(rows):
        for col in range(cols):

            if board[row][col] == word[0]:
                if dfs(row, col, 0):
                    return True

    return False


board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCCED"

print(exist(board, word))























