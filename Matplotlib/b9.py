import matplotlib.pyplot as plt
import numpy as np

divisions =["Div-A", "Div-B", "Div-C", "Div-D", "Div-E"]
divisions_average_marks =[70, 82, 73, 65, 68]
variance = [5,8,7,6,4]

plt.barh(divisions, divisions_average_marks, color="red")
plt.title("Bar graph")
plt.xlabel("Divisions")
plt.ylabel("Marks")
plt.show()