x= [2,6,3,8,1,4,7]
len(x)

for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if(x[i]> x[j]):
            t=x[i]
            x[i]=x[j]
            x[j]=t
print(x)
