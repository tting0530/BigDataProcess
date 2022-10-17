#!/bin/user/python3

con_sum=0.0
con_count = 0

with open("mbox-short.txt", "rt") as fp:
	for line in fp:
		if line.startswith("X-DSPAM-Confidence: "):
			#print(line)
			str_arr = line.split()
			#print(str_arr[1])
			con_sum += float(str_arr[1])
			con_count += 1

print(con_sum / con_count);
	
