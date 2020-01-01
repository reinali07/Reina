def genSortKey(col,up):
	def key(x):
		if up:
			return x[col]
		else:
			return -x[col]
	return key
sortKey = genSortKey(3,False)

m = [[1,5,3,7,6],[6,3,1,5,6],[8,5,2,6,4]]

sortm = sorted(m,key=sortKey)

print(sortm)
