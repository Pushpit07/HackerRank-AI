def nextMove(n,r,c,grid):
    row_m = r
    col_m = c
    
    col_p = row_p = 0

    for i in range(n):
        line = len(grid[i])
        for j in range(line):
            if grid[i][j] == 'p':
                row_p = i
                col_p = j

    if row_m < row_p:
        row_m = row_m + 1
        return 'DOWN'
    
    elif row_m > row_p:
        row_m = row_m - 1
        return 'UP'

    
    if col_m < col_p:
        col_m = col_m + 1
        return 'RIGHT'
    
    elif col_m > col_p:
        col_m = col_m - 1
        return 'LEFT'

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))