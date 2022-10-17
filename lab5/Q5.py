#!/usr/bin/python3

import json

with open("movie.json", "rt") as datafile:
	jsondata = json.load(datafile) 

movies = list(jsondata["movie"])
sum = 0
#in 다음에 바로 dic을 넣으면 그 값이 들어가는듯
for i in range(3):
	movie = movies[i] #한번에 sum에 넣도록 쓸 수는 없나?
	#tmp2 = tmp["salesAmt"]
	sum += int(movie["salesAmt"] )

print("오늘 매출액은 총 {} ".format(sum), "원")
