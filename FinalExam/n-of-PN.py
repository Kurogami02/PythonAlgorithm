import math
def PN(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True
n = int(input("Nhập số nguyên dương n = "))
temp = 0
i=2
list = []
while (temp < n):
    if (PN(i)):
        list.append(str(i))
        temp = temp + 1
    i = i + 1
print (n, "số nguyên tố đầu tiên là: ", end='')
print (', '.join(list))