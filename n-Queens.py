def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()


def is_safe(board, row, col, n):
    # Check the left side of the current row
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, n):
    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_nqueens(board, col + 1, n):
                return True

            board[row][col] = 0  # Backtrack

    return False


n = int(input("Enter value of N: "))
board = [[0 for _ in range(n)] for _ in range(n)]

# Place the first queen at the top-left corner
board[0][0] = 1

if solve_nqueens(board, 1, n):
    print("\nN-Queens Solution:")
    print_board(board, n)
else:
    print("No solution exists with the first queen at (1, 1).")
