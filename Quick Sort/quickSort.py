def ordena(v,i,f):
	a = i-1
	pivot = v[f]
	
	for j in range(i,f):
		if v[j] <= pivot:
			a+=1
			v[a],v[j] = v[j], v[a]

	v[a+1], v[f] = v[f], v[a+1]	

	return a+1

def quick(v,i,f):
	if i < f:
		m = ordena(v,i,f)
		quick(v,i,m-1)
		quick(v,m+1,f)


if __name__=="__main__":
	
	v = [4,5,3,6,2,7,8,1,9,0]
	tam = len(v)
	
	print(v)	
	quick(v,0,tam-1)
	print()
	print(v)

	

