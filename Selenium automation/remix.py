s=list(map(str,input().split()))
minl=len(s[0])
mins=s[0]
for i in s:
	x=len(i)
	if x<minl:
		minl=x
		mins=i
print(mins,end=" ")
for i in s:
	print(i,mins,end=" ")