import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
incomes[9995]=600
incomes[9996]=600
incomes[9997]=600
incomes[9998]=600
incomes[9999]=600
plt.hist(incomes,bins=50) 
mean1=np.mean(incomes)
median=np.median(incomes)
