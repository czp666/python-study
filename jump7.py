i=0
for i in range(1,100):
	i+=1
	if(i%7==0):continue
	elif i%10==7: continue
	elif i//10%10==7: continue
	else: print(i)
