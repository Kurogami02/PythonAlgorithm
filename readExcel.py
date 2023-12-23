import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = 'D:\Office\Course\ML\DTPT.xlsx' 
df = pd.read_excel(excel_file_path)
df = df.drop(df.columns[0], axis=1)
df['Thành tiền'] = df['Đơn giá'] * df['Số lượng']
tongtien = df['Thành tiền'].sum()
df.at[df.index[-1], 'Thành tiền'] = tongtien
print(df.head())

df_khongcohangtongtien = df.drop(df.index[-1]) #phải xóa hàng tổng tiền cuối cùng đi để lấy dữ liệu cột thành tiền đúng
plt.pie(df_khongcohangtongtien['Thành tiền'], labels=df_khongcohangtongtien['Tên hàng'], autopct='%1.1f%%', startangle=50)
plt.axis('equal')  # Để biểu đồ tròn hiển thị đúng tỷ lệ
plt.title('Biểu đồ doanh thu')
plt.tight_layout()
plt.show()