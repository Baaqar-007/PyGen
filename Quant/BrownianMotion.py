import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import seaborn as sns 

rng = np.random.default_rng(42) # pseudo-random geenrator for seed value 

paths = 50
points = 1000 # number of time steps per path

# Standard Brownian Motion
mu, sigma = 0.0, 1.0 # mean and standard deviation 

Z = rng.normal(mu,sigma, (paths,points)) # normal Gaussiona distribution 

interval = [0.0,1,0]  # time interval for the simulation
dt = (interval[1] - interval[0]) / (points-1) 

t_axis = np.linspace(interval[0], interval[1], points)  # creates points numbers of equally space points  

W = np.zeros((paths, points))
for idx in range(points-1):
    real_idx = idx + 1 
    W[:, real_idx] = W[:, real_idx -1] + np.sqrt(dt)* Z[:,idx]
    # This line updates each row of column real_idx in W. It takes the corresponding row value from the previous column (real_idx - 1), 
    # adds the square root of dt multiplied by the corresponding row value from column idx of Z.
    
fig, ax = plt.subplots(1,1, figsize = (12,8))
for path in range(paths):
    ax.plot(t_axis, W[path,:])
ax.set_title("Standard Brownian Motion sample paths")
ax.set_xlabel("Time")
ax.set_ylabel("Asset Value") 
plt.show()