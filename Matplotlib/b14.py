import matplotlib.pyplot as plt
import numpy as np
height = np.array([167, 178, 149, 165, 155, 186, 166, 146,159,185,145,168, 172, 181, 169]) 
weight = np.array([86,74,66,78,68, 79, 90, 73,70,88,66,84,67,84,77]) 
plt.xlim(140, 200) 
plt.ylim(60, 100) 
plt.scatter (height, weight) 
plt.title("Scatter Plot") 
plt.xlabel("Height") 
plt.ylabel("Weight") 
plt.show()
