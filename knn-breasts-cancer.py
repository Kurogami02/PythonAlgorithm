import csv
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Đọc dữ liệu từ file CSV và xử lý
def load_data(path):
    with open(path, "r") as file:
        data = list(csv.reader(file))
    
    # Loại bỏ hàng đầu tiên (tiêu đề cột)
    data = data[1:]
    
    # Tách features và labels
    features = np.array([row[2:] for row in data], dtype=float)
    labels = np.array([1 if row[1] == 'M' else 0 for row in data])
    
    return features, labels

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
def split_data(features, labels):
    return train_test_split(features, labels, test_size=0.2, random_state=42)

# Hàm tính độ chính xác của mô hình
def evaluate_model(train_features, test_features, train_labels, test_labels, k):
    # Xây dựng mô hình k-NN với giá trị k
    model = KNeighborsClassifier(n_neighbors=k)
    
    # Huấn luyện mô hình
    model.fit(train_features, train_labels)
    
    # Dự đoán nhãn trên tập kiểm tra
    predictions = model.predict(test_features)
    
    # Tính độ chính xác
    accuracy = accuracy_score(test_labels, predictions)
    
    return accuracy

if __name__ == "__main__":
    # Load dữ liệu từ file CSV
    features, labels = load_data("D:\Office\Course\ML/data.csv")
    
    # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
    train_features, test_features, train_labels, test_labels = split_data(features, labels)
    
    # Thử nghiệm các giá trị k khác nhau và chọn giá trị k tốt nhất
    best_accuracy = 0
    best_k = 0
    
    for k in range(1, 21):
        accuracy = evaluate_model(train_features, test_features, train_labels, test_labels, k)
        print(f"K = {k}, Accuracy = {accuracy}")
        
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k
    
    print(f"Best K: {best_k}, Best Accuracy: {best_accuracy}")