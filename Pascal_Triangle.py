
r = int(input()) 
a=[]

for i in range(r):
	temp=[]
	for j in range(i+1):
		if j==0 or j==i:
			temp.append(1)
		else:
			temp.append(a[i-1][j-1] + a[i-1][j])
	a.append(temp)	
	


for i in range(r):
	for j in range(r-1-i):
		print('',end=' ')
	for j in range(i+1):
		print(a[i][j],end=' ')
	print("")
	



		
