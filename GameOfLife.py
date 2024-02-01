import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            if grid[i, j]  == 255:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 255
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

N = 500
updateInterval = 500
grid = np.array([])
grid = np.random.choice([0,255], N*N, p=[0.2, 0.8]).reshape(N, N)

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                              frames = 100,
                              interval=updateInterval,
                              save_count=50)

plt.show()

"""
Conway’s Game of Life is a cellular automaton devised by the British mathematician John Horton Conway. It’s a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. 
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent.

The rules of the game are as follows:

Birth: A dead cell with exactly three live neighbors becomes a live cell (as if by reproduction).
Survival: A live cell with two or three live neighbors stays alive (as if by survival).
Death: In all other cases, a cell dies or remains dead (overcrowding or loneliness).

These simple rules give rise to complex behaviors which have been the subject of much interest since the Game of Life’s inception. It’s a classic example of emergence and self-organization. It’s interesting for both computer scientists, mathematicians, and the general public. 
The Game of Life is Turing complete, which means given enough resources, it can simulate a Turing machine, and therefore, theoretically can compute anything that can be computed!
"""