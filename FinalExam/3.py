name= []
n=0
inputname = input("Nhập tên đầy đủ: ")
name = inputname.split()
for i in range(0,len(name)):
    n=n*10+len(name[i])
str1 = str(n)
str2 = str1[::-1]
print("Tên của em là: ", end='')
print (' '.join(name))
print("Độ dài kí tự trong tên em lần lượt là:",n)
if (str1 == str2):
    print(n,"\nlà số thuận nghịch")
else:
    print(n,"không là số thuận nghịch")