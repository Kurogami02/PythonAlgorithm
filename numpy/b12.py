import numpy as np

np.random.randint(0, 2) # Ngẫu nhiên số nguyên trong khoảng [0, 2)

coins = np.random.randint(2, size=1000) 
print(coins.shape)
#gieo ngẫu nhiên 1000 lần random, lấy ví dụ đồng xu, ngửa là 0, sấp là 1

print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)
#Out:
    #% số lần tung được mặt ngửa:  51.5
    #% số lần tung được mặt úp:  48.5

coins = np.random.choice([0, 1], size=1000, p=[0.2, 0.8]) # random.choice sẽ lấy ngẫu nhiên các phần tử trong mảng ở tham số đầu tiên với xác suất ở tham số p
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)
#Out: % số lần tung được mặt ngửa:  20.3
    #% số lần tung được mặt úp:  79.7