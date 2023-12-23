import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt

# Đọc dữ liệu: Dùng Panda đọc dữ liệu, đưa vào Frame và in ra
data = pd.read_csv('D:\Office\Course\ML/data.csv')
print(data.info())

# Tách data thành 2 phần x chứa các thuộc tính và y chứa các nhãn
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

#  (testing set) sử dụng hàm train_test_split từ thư viện sklearn.
# Tách data ra làm 2 phần train và test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Dùng StandardScaler để chuẩn hóa dữ liệu
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Dùng for để train mô hình và tính toán tỉ lệ lỗi và in ra đồ thị
error_rate = []
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

# Train và dán nhãn cho từng tập data, in ra ma trận
plt.figure(figsize=(10,6))
plt.plot(range(1,40), error_rate, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

best_k = error_rate.index(min(error_rate)) + 1  # Chọn giá trị K có er nhỏ nhất
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nPhân loại:\n", classification_report(y_test, y_pred))
print("\nTỷ lệ:", accuracy_score(y_test, y_pred))