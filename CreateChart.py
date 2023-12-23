import matplotlib.pyplot as plt
import pandas as pd

excel = 'D:\Office\Course\ML\DTPT.xlsx'
df = pd.read_excel(excel)

plt.figure(figsize=(4,4))
plt.pie (df['Số lượng'], labels=['Tên hàng'], autopct='%1.1f%%', startangle=140)

plt.title('Biểu đồ tròn')

plt.show()
