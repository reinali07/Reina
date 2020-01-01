def sortr(L):
	buckets = [[],[],[],[],[],[],[],[],[],[]]
	length = len(str(abs(max(L))))
	for i in range(0,length,1):
		for j in L:
			buckets[j//10**i%10] += [j]
		index = 0
		for j in range(0,len(buckets),1):
			for h in range(0,len(buckets[j]),1):
				L[index] = buckets[j][h]
				index+=1
		buckets = [[],[],[],[],[],[],[],[],[],[]]
	return True

#L = [1,3,5235,43,65,74,13,8,2,3,434,11,2344,65,8678,34,467,54,66,79]
#sortr(L)
#print(L)
