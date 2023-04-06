import math
n= int(input("Nhập n: "))
listFi=[]
i=0
s1=0 
s2=1
FPN=[]
if n<0:
    print("Không có số fibonacci nhỏ hơn 0")
    n= int(input("Nhập lại n: "))
while s1<n:
    listFi.append(s1)
    s=s1+s2
    s1=s2
    s2=s
if len(listFi)>3:
    for i in range(3,len(listFi)):
        x=0
        for j in range(1,listFi[i]):
            if listFi[i]%j==0:
                x=x+1
        if x==1:
            FPN.append(str(listFi[i]))
print ("Dãy số fibonacci là số nguyên tố <",n,"là: ", end='')
print (', '.join(FPN))