from math import factorial
n= int(input("Nhập n: "))
GT=1
if n<0:
    print("Số nguyên âm không có giai thừa.")
    n= int(input("Nhập lại: "))
if n==0:
    print("Giai thừa của 0 là:", GT)
else:
    for i in range (1, n+1):
        GT=GT*i
print("Giai thừa",n ,"là:",GT)