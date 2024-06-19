def print_sudoku(sudoku):
    print("\n\n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j]) + " "
        print(line)
    print("\n\n")

def find_next_cell_to_fill(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1

def is_valid(sudoku, i, j, e):
    row_ok = all([e != sudoku[i][x] for x in range(9)])
    if row_ok:
        column_ok = all([e != sudoku[x][j] for x in range(9)])
        if column_ok:
            sec_top_x, sec_top_y = 3 * (i // 3), 3 * (j // 3)
            for x in range(sec_top_x, sec_top_x + 3):
                for y in range(sec_top_y, sec_top_y + 3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False

def solve_sudoku(sudoku, i=0, j=0):
    i, j = find_next_cell_to_fill(sudoku)
    if i == -1:
        return True
    for e in range(1, 10):
        if is_valid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solve_sudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False

def input_sudoku():
    sudoku = []
    print("Enter the Sudoku puzzle row by row (use 0 to represent empty cells):")
    for _ in range(9):
        row = list(map(int, input().split()))
        sudoku.append(row)
    return sudoku

if __name__ == "__main__":
    # Input Sudoku puzzle
    print("Input Sudoku puzzle:")
    unsolved_sudoku = input_sudoku()

    # Solve the Sudoku puzzle
    if solve_sudoku(unsolved_sudoku):
        print("\nSudoku puzzle solved successfully!")
        # Print the solved Sudoku grid
        print("\nSolved Sudoku:")
        print_sudoku(unsolved_sudoku)
    else:
        print("\nNo solution exists for the given Sudoku puzzle.")
