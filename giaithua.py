def giaithua(n):
    if n <= 1: 
       return 1 
    else: 
        return (n * giaithua(n-1))
num1 = int(input("Nhập số cần tính giai thừa: "))
print("Giai thừa của", num1, "là", giaithua(num1))
