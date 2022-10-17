#!/usr/bin/python3

a=[]
b=[]
dic={}

for i in range(10):
	a.append(i+1)
	b.append((i+1)*(i+1))

for i in range(10):
	dic[a[i]] = b[i]
#print(dic.get(6))
print(dic[6])

#왜 range(1, 11)로 헸을때는 아예 오류가 나는가
