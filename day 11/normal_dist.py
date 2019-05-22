import numpy as np 
import matplotlib.pyplot as plt
data = np.random.normal(150,20,1000)
plt.hist(data,bins=100) 
y=np.std(data)
z=y**2
