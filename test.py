x=int(input("Nhập số cần đảo ngược: "));
n=0;
t=int;
while(x>=1):
    t=x%10;
    n=n*10+t;
    x=x//10;
print('Số sau khi đảo ngược: ',n);