name = input("Tên em là: ")
n=int(len(name))
d = dict()
for i in range(1, n + 1):
    d[i] = i * i
print ("Tên của em là:",name)
print ("Tên",name,"có độ dài là:",n)
print ("Dictionary của",n,"là:",d)