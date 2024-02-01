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
    # this line plots the data from the path-th row of W against t_axis on the subplot ax
ax.set_title("Standard Brownian Motion sample paths")
ax.set_xlabel("Time")
ax.set_ylabel("Asset Value") 
# plt.show()

final_values = pd.DataFrame({'final_values': W[:, -1]}) # sample path ending values
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
sns.kdeplot(data=final_values, x='final_values', fill=True, ax=ax)
ax.set_title("Kernel Density Estimate of asset path final value distribution")
ax.set_ylim(0.0, 0.325)
ax.set_xlabel('Final Values of Asset Paths')
# plt.show()
# print(final_values.mean(),final_values.std()) # increasing the number of paths , makes mean and std approach their assumed values due to law of laege numbers

mu_c, sigma_c = 0.1,0.1 # mean and standard deviation
X = np.zeros((paths, points))
for idx in range(points - 1):
    real_idx = idx + 1
    X[:, real_idx] = X[:, real_idx - 1] + mu_c * dt + sigma_c * np.sqrt(dt) * Z[:, idx] 
    

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
for path in range(paths):
    ax.plot(t_axis, X[path, :])
ax.set_title("Constant mean and standard deviation Brownian Motion sample paths")
ax.set_xlabel("Time")
ax.set_ylabel("Asset Value")
plt.show()