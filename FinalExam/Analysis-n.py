import math
n= int(input("Nhập n: "))
listPN=[]
i=2
origin=n
if n<=1:
    listPN=str(n)
else:
    for i in range(i, n+1):
        temp =0
        while n%i==0:
            temp=temp+1
            n=n//i
            listPN.append(str(i))
print (origin,"= ", end='')
print (' x '.join(listPN))