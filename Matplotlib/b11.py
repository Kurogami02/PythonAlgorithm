import matplotlib.pyplot as plt
import numpy as np

divisions =["Div-A", "Div-B", "Div-C", "Div-D", "Div-E"]
boys_average_marks=[68,67,77,61,70]
girls_average_marks=[72, 97, 69, 69, 66]

index=np.arange(5)
width=0.30

plt.bar(index, boys_average_marks, width, color="orange", label="Boys marks")
plt.bar(index, girls_average_marks, width, color="blue", label="Girls marks",  bottom=boys_average_marks)

plt.title("Horizontally Stacked Bar Graphs")
plt.ylabel("Marks")
plt.xlabel("Divisions")
plt.xticks(index, divisions)

plt.legend(loc="best")
plt.show()