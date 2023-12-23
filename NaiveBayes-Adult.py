import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df=pd.read_csv("D:\Office\Course\ML/adult.csv") #đọc dữ liệu từ data set
df.head()

#Chuyển đổi tên cột thành các phần tử dạng String trong mảng
col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship',
             'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']

df.columns = col_names

df.columns

df.isnull().sum()

categorical = [var for var in df.columns if df[var].dtype=='O']

print('There are {} categorical variables\n'.format(len(categorical)))

print('The categorical variables are :\n\n', categorical)

df[categorical].isnull().sum()

X = df.drop(['income'], axis=1)

y = df['income']

from sklearn.model_selection import train_test_split

#Tách dữ liệu thành 2 tập train(8) và test(2) với tỉ lệ 8:2
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

import category_encoders as ce #Thêm vào thư viện Encoders

#Chuyển đổi các biến phân loại thành các biến số nhị phân bằng cách sử dụng One-hot encoder.
encoder = ce.OneHotEncoder(cols=['workclass', 'education', 'marital_status', 'occupation', 'relationship', 
                                 'race', 'sex', 'native_country'])

X_train = encoder.fit_transform(X_train)

X_test = encoder.transform(X_test)

from sklearn.naive_bayes import GaussianNB

# Khởi tạo mô hình NB sử dụng phương pháp Gaussian
gnb = GaussianNB()
# Huấn luyện mô hình bằng tập huấn luyện
gnb.fit(X_train, y_train)

# Dự đoán nhãn lớp cho các mẫu trong tập kiểm tra.
y_pred = gnb.predict(X_test)

y_pred

from sklearn.metrics import accuracy_score

print('Độ chính xác mô hình: {0:0.2f}%'. format(accuracy_score(y_test, y_pred)*100))

print('Tỉ lệ phần tử của train set: {:.2f}%'.format(gnb.score(X_train, y_train)*100))

print('Độ chính xác test: {:.2f}%'.format(gnb.score(X_test, y_test)*100))

