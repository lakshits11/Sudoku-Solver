grid_sudoku = [
    [4, 0, 5, 0, 9, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 4, 0, 3, 5, 0],
    [0, 0, 3, 0, 0, 5, 0, 0, 0],
    [0, 0, 9, 6, 0, 3, 8, 0, 0],
    [0, 0, 0, 2, 0, 0, 7, 0, 0],
    [0, 3, 1, 0, 5, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 3, 0, 9, 0, 1],
]


def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def valid(board, value, pos):

    # Checking row
    for i in range(9):
        if board[pos[0]][i] == value and pos[1] != i:
            return False
    
    # Checking col
    for i in range(9):
        if board[i][pos[1]] == value and pos[1] != i:
            return False

    # Check board
    boardx_x = pos[1] // 3
    boardx_y = pos[0] // 3

    for i in range(boardx_y * 3, boardx_y * 3 + 3):
        for j in range(boardx_x * 3, boardx_x * 3 + 3):
            if board[i][j] == value and (i, j) != pos:
                return False

    return True


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)

    return None


def print_grid(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


if __name__ == "__main__":
    print("Given Unsolved Board:")
    print_grid(grid_sudoku)
    print("\nSolving the Sudoku...\n")
    solve_sudoku(grid_sudoku)
    print_grid(grid_sudoku)
