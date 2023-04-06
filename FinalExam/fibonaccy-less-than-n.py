import math
import re
n= int(input("Nhập n: "))
i=0
if n<0:
    print("Không có số fibonacci nhỏ hơn 0")
    n= int(input("Nhập lại n: "))
def fbnc(n):
    if (n == 0 or n == 1):
        return n
    else:
        return fbnc(n - 1) + fbnc(n - 2)
def Pnum(n):
    if n==2:
        return True
    elif n<2 or n%2==0:
        return False
    for i in range(3, n, 2):
        if (n % i == 0):
            return False
        return True
fin = fbnc(i)
while(fin < n):
    fin = fbnc(i)
    if (Pnum(fin)):
        print(fin)
    i = i + 1