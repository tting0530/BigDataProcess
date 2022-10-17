#!/usr/bin/python3

import datetime as d
#두번째 datetime은 뭐지?
now = d.datetime.now()
birth = d.datetime(1994, 5, 5)
#print(birth)
#print(now)

birth_to_now = now - birth
print(birth_to_now)
