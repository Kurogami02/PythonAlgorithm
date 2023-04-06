name= []
n=0
inputname = input("Nhập tên: ")
name = inputname.split()
for i in range(0,len(name)):
    n=n*10+len(name[i])
S=0
temp=n
while(n>0):
    S=S+n%10
    n=n//10
print("Tên của em là: ", end='')
print (' '.join(name))
print("Độ dài kí tự trong tên em lần lượt là:",temp,'có tổng là:',S)