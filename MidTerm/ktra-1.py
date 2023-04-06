A=[1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
A.sort();
b=[];
c=[];
for i in range(0,len(A)):
    if A[i]<30:
        b.append(A[i]);
    else:
        break;
print('\nCac so nho hon 30:',b);
x=int(input("Nhap 1 so bat ky:"));
print('Cac so lon hon',x,'la:');
for i in range(0, len(A)):
    if A[i] > x :
        c.append(A[i]);
print(' ',c);
