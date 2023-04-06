import re
nameid=input("Nhập vào chuỗi tên và id: ")
id=[]
name=[]
id=re.sub(r'\D','', nameid)
name=nameid.strip(id)
l=re.findall(r'\d',id)
idsplit=tuple(l)
namesplit=tuple(name)
print("Tên em là:",name)
print("",namesplit)
print("Mã sinh viên là:",id)
print (l)
print ("",idsplit)