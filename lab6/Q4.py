#!/usr/bin/python3

n1, n2 = input("숫자 두 개를 입력하세요 : ").split()
n1= int(n1)
n2=int(n2)
try:
	print(float(n1/n2))
except ZeroDivisionError as e:
	print(e)

