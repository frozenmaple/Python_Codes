import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N=3
ON = 255
OFF = 0
vals = [ON, OFF]

grid = np.array([[0, 0, 0],[255,  255, 0],[0,  255, 0]])
#print(grid)

newGrid = grid.copy()


for i in range(N):
        for j in range(N):
            # compute 8-neghbor sum
            # using toroidal boundary conditions - x and y wrap around
            # so that the simulaton takes place on a toroidal surface.
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / 255)
            # apply Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

print(newGrid)
print(id(newGrid))

grid = newGrid.copy()
grid2 = []
grid2[:] = newGrid[:]

print(grid)
print(id(grid))
#print('\n')
print(id(grid2))


