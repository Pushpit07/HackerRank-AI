#!/usr/bin/python
import math
# Head ends here

def calculate_distances(posr, posc, dirty_cells):
    nearest_dirty_cell = []
    for i in range(len(dirty_cells)):
        # Euclidean distance
        result = math.sqrt(((dirty_cells[i][0] - posr) ** 2) + ((dirty_cells[i][1] - posc) ** 2))
        nearest_dirty_cell.append(result)
    return [x for (y, x) in sorted(zip(nearest_dirty_cell, dirty_cells))]

# Set the bot in your new position
def next_move(posr, posc, board):
    dirty_cells = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'd':
                dirty_cells.append([i, j])

    next_dirt = calculate_distances(posr, posc, dirty_cells)

    if next_dirt[0][1] < posc:
        print('LEFT')
    elif next_dirt[0][1]  > posc:
        print('RIGHT')
    elif next_dirt[0][0] < posr:
        print('UP')
    elif next_dirt[0][0] > posr:
        print('DOWN')
    else:
        print('CLEAN')

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)