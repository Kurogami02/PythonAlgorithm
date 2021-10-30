import matplotlib.pyplot as plt
import numpy as np
firms = ["Firm A", "Firm B", "Firm C", "Firm D","Firm E"] 
market_share = [20, 25, 15, 10, 20]
Explode = [0,0.1,0,0,0] 
plt.pie (market_share, explode=Explode, labels=firms, shadow=True, startangle=45) 
plt.axis('equal') 
plt.legend(title="List of Firms")
plt.show()
