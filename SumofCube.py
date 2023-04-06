def sum(n):
    if n == 1: 
       return 1 
    else: 
        return (n*n*n + sum(n-1))
num1 = int(input("Nhập số cần tính tổng: "))
print("tổng của", num1, "là", sum(num1))