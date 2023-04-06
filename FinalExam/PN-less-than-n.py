import math
n= int(input("Nhập n: "))
PN=[]
if n<=2:
    print("Không có số nguyên tố nhỏ hơn 2!")
else:
    for i in range(2,n):
        x=0
        for j in range(1,i+1):
            if i%j==0:
                x=x+1
        if x==2:
            PN.append(str(j))
print ("Dãy số nguyên tố <",n,"là: ", end='')
print (', '.join(PN))