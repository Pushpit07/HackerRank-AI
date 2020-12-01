#!/usr/bin/python
from math import floor

def displayPathtoPrincess(n,grid):
    found = 0
    
    if grid[0][0] == 'p':
        found = 1
    elif grid[0][n-1] == 'p':
        found = 2
    elif grid[n-1][0] == 'p':
        found = 3
    else:
        found = 4
        
    if found == 1:
        for i in range(floor(n/2), 0, -1):
            print("UP");
        for j in range(floor(n/2), 0, -1):
            print("LEFT");

    elif found == 2:
        for i in range(floor(n/2), 0, -1):
            print("UP");
        for j in range(floor(n/2), 0, -1):
            print("RIGHT");

    elif found == 3:
        for i in range(floor(n/2), 0, -1):
            print("DOWN");
        for j in range(floor(n/2), 0, -1):
            print("LEFT");
            
    elif found == 4:
        for i in range(floor(n/2), 0, -1):
            print("DOWN");
        for j in range(floor(n/2), 0, -1):
            print("RIGHT");

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)