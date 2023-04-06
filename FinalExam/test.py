import math
def fibonacci(n):
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
def isPrimeNumber(n):
    if (n < 2):
        return False;
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True;
n = int(input("Nhập số nguyên dương n = "));
print ("Tất cả các số fibonacci nhỏ hơn", n, "và nguyên tố:");
i = 0;
fin = fibonacci(i);
while(fin < n):
    fin = fibonacci(i);
    if (isPrimeNumber(fin)):
        print(fin)
    i = i + 1;