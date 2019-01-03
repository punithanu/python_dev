l=[]
for i in range(2000, 3500):
	if(i%7 == 0) and (i%5 != 0):
		l.append(str(i))
print l
