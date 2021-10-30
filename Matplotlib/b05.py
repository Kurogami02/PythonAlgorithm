import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
y=x**3
plt.subplot(1,2,1) 
plt.plot([1,2,3,4],[1,4,9,16], "go") 
plt.title("1st subplot")
plt.subplot(1,2,2) 
plt.plot(x,y,"r^") 
plt.title("2nd subplot") 
plt.suptitle("My sub-plots") 
plt.show()
