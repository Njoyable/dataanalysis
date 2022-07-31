import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


def init():
    brett = np.random.choice([0, 1], 52*52).reshape(52,52)
    return brett

def count(brett, i, j):
    count = 0
    count += brett[i-1][j-1] + brett[i-1][j] + brett[i+1][j+1] + brett[i][j-1] + brett[i][j+1] + brett[i+1][j-1] + brett[i+1][j] + brett[i+1][j+1] 
    return count

def evolve(brett):
    brett_neu = np.zeros((52,52))
    for i in range(1,51):
        for j in range(1,51):
            if count(brett,i,j) == 2 or count(brett,i,j) == 3 and brett[i][j] == 1:
                brett_neu[i][j] = 1
            elif brett[i][j] == 0 and count(brett,i,j) == 3:
                brett_neu[i][j] = 1
    return brett_neu
               
 
# fig = plt.figure()
brett = init()

start = time.time()

for l in range(1000):
    for k in range(800):
        brett = evolve(brett)

end = time.time()

print(end-start)

# anim = FuncAnimation(fig,evolve, blit = True)
