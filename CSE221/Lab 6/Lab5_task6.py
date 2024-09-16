# task 6

def dfs(grid, row, column, r, c):
    # '_' means already visited
    if grid[r][c] == '.':
        grid[r][c] = "_"
    elif grid[r][c] == 'D':
        grid[r][c] = "d"

    diamond_count = 0

    if c+1 < column and (grid[r][c+1] == '.' or grid[r][c+1] == 'D'):  # right
        diamond_count += dfs(grid, row, column, r, c+1)
    if c-1 >= 0 and (grid[r][c-1] == '.'or grid[r][c-1] == 'D'):  # left
        diamond_count += dfs(grid, row, column, r, c-1)
    if r+1 < row and (grid[r+1][c] == '.' or grid[r+1][c] == 'D'):  # down
        diamond_count += dfs(grid, row, column, r+1, c)
    if r-1 >= 0 and (grid[r-1][c] == '.' or grid[r-1][c] == 'D'):  # up
        diamond_count += dfs(grid, row, column, r-1, c)

    if grid[r][c] == "d":
        diamond_count += 1
        grid[r][c] = "_"

    return diamond_count


input_file = open("Lab5_task6_input6.txt", "r")
output_file = open("Lab5_task6_output6.txt", "w")

row, column = list(map(int, input_file.readline().split()))
grid = []
for r in range(row):
    grid.append(list(input_file.readline()))
    if grid[-1][-1] == '\n':
        grid[-1].pop()

maximum_diamond = 0

for r in range(row):
    for c in range(column):
        if grid[r][c] in ['.', 'D']:
            count = dfs(grid, row, column, r, c)
            if count > maximum_diamond:
                maximum_diamond = count

print(maximum_diamond, file = output_file)