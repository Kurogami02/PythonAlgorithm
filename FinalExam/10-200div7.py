list = []
for i in range(10, 200+1):
    if (i % 7 == 0) and (i % 5 != 0):
        list.append(str(i))
print ("Dãy số chia hết cho 7 ko là bội của 5: ", end='')
print (', '.join(list))