A=[1,1,2,3,5,8,13,21,34,55,88];
B=[1,3,5,4,7,88,66,59,40,54];
A.sort();
B.sort();
C=[];
D=[];
E=[];
for i in range(0,len(A)):
    for j in range(0,len(B)):
        if A[i]==B[j]:
            C.append(A[i]);
            break;
for i in range(0,len(A)):
    f=0;
    for j in range(0,len(C)):
        if A[i]==C[j]:
            f=1;
    if f!=1:
        D.append(A[i]);
for i in range(0, len(B)):
    f=0
    for j in range(0, len(C)):
        if B[i]==C[j]:
            f=1
    if f!= 1:
        E.append(B[i]);
print('\nCac pt trung nhau: ',C);
print('A sau khi xoa: ',D);
print('B sau khi xoa: ',E);