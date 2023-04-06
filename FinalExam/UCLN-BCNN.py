from unittest import result


a= int(input("Nhập số thứ nhất:"))
b= int(input("Nhập số thứ hai:"))
def UCLN(a,b):
    if a==0 or b==0:
        return a +b
    else:
        while a!=b:
            if a>b:
                a=a-b
            else: 
                b=b-a
        return a
def BCNN(a,b):
    result=UCLN(a,b)
    return a*b//result
print("Ước số chung lớn nhất là:",UCLN(a,b))
print("\nBội số chung nhỏ nhất là:",BCNN(a,b))