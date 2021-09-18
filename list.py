x= [2,6,3,8,1,4,7]
a= len(x)

for i in range(0,a-1):
    for j in range(i+1,a):
        if(x[i]> x[j]):
            b=x[i]
            x[i]=x[j]
            x[j]=b
print(x)
