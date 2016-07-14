# Backtracking's back (recursive solution)
import copy

grid_sum = 0
temp_original_grid = None


with open("p096_sudoku.txt", 'r') as f:
    lines = f.readlines()

def is_safe(grid, x, y, num):
    in_square = False
    for ix in range(x-x%3, x-x%3+3):
        for iy in range(y-y%3, y-y%3+3):
            if num == grid[iy][ix]:
                in_square = True

    in_row = num in grid[y]
    in_col = num in [grid[i][x] for i in range(9)]

    return not in_square and not in_row and not in_col


def pretty_print(grid):
    for i in range(9):
        original_grid_row = ' '.join(str(a) for a in temp_original_grid[i])
        original_grid_row = original_grid_row.replace('0', '.')
        grid_row = ' '.join(str(a) for a in grid[i])
        print(original_grid_row + '\t\t\t' + grid_row)


def solve_grid(grid, x, y):
    if 0 not in grid[8]:  # Solved
        pretty_print(grid)
        three_digit = 100*grid[0][0] + 10*grid[0][1] + grid[0][2]
        print(three_digit)
        print()

        global grid_sum
        grid_sum += three_digit

        return True

    # Move to next empty square
    while grid[y][x]:
        x += 1
        if x == 9:
            x = 0
            y += 1

    for num in range(1, 10):
        if is_safe(grid, x, y, num):
            grid[y][x] = num

            #print(grid[y][x])
            if (solve_grid(grid, x, y)):  # Next solution is valid
                return True

            grid[y][x] = 0  # Remove this solution

    return False  # Backtrack


for li in range(0, 500, 10):
    print(lines[li].rstrip())
    grid = [[int(b) for b in a.rstrip()] for a in lines[li+1:li+10]]
    temp_original_grid = copy.deepcopy(grid)
    solve_grid(grid, 0, 0)

print(grid_sum)
