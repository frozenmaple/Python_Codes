import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON =255
OFF = 0
vals = [ON,OFF]

def randomGrid(N):
    return np.random.choice(vals, N*N, p=[0.2,0.8]).reshape(N,N)

def addGlider(i,j,grid):
    glider = np.array([[0,0,255],[255,0,255],[0,255,255]])
    grid[i:i+3,j,j+3] = glider

def update(frameNum,img,grid,N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int( ( grid[(i-1)%N,(j-1)%N] + grid[(i-1)%N,j] \
                         + grid[(i-1)%N,(j+1)%N] + grid[i,(j-1)%N] \
                         + grid[i,(j+1)%N] + grid[(i+1)%N,(j-1)%N] \
                         + grid[(i+1)%N,j] + grid[(i+1)%N,(j+1)%N] )/255 )
            if grid[i,j] == ON:
                if (total<2) or (total>3):
                    newGrid[i,j] = OFF
            else:
                if total == 3:
                    newGrid[i,j] = ON
    
    img.set_data(newGrid)
    grid[:] = 
            