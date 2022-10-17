#!/bin/user/python3

con_sum=0.0
con_count = 0
dic={}
#사전 검색은 .get()으로!
with open("mbox-short.txt", "rt") as fp:
	for line in fp:
		if line.startswith("Author: "):
			#print(line)
			str_arr = line.split()
#			print(str_arr[1])
		
			if str_arr[1] in dic:
				dic[str_arr[1]] += 1
			else:
				dic[str_arr[1]] = 1
#			print(dic.get(str_arr[1]))
#			print(str_arr[1])

print(dic);
	
