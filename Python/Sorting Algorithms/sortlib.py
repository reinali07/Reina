def selection_sort(u):
	for iniU in range(0,len(u),1):
		positionOfMin = iniU
		for i in range(iniU,len(u),1):
			if u[i] < u[positionOfMin]:
				positionOfMin = i
		old = u[iniU]
		u[iniU] = u[positionOfMin]
		u[positionOfMin] = old		
	return True

def helper_heapify(u,end):
	for i in range(0,end,1):
		x = i
		while True:
			parent = int((x-1)/2)
			if u[x] > u[parent]:
				u[x],u[parent] = u[parent],u[x]
				x = parent
			else:
				break
	return True
def heapify(u):
	helper_heapify(u,len(u))
	return True
def reheapify(u,end):
	helper_heapify(u,end)
	return True
def heap_sort(u):
	heapify(u)
	#print(u)
	for iniS in range(len(u)-1,-1,-1):
		u[0],u[iniS] = u[iniS],u[0]
		reheapify(u,iniS)
		#print(u)
	return True

#def helper_merge(l1,l2):
#	l1end = 0
#	l2end = 0
#	while l1end < len(l1) and l2end < len(l2):
#		if l1[l1end] < l2[l2end]:
#			accum += [l1[l1end]]
#			l1end += 1
#		else:
#			accum += [l2[l2end]]
#			l2end += 1
#	if l1end < len(l1):
#		accum += l1[l1end:]
#	elif l2end<len(l2):
#		accum += l2[l2end:]
#	return accum
def merge_sort(u):
	if len(u) <= 1:
		return u

	UL = u[int(len(u)/2):]
	LL = u[:int(len(u)/2)]
	merge_sort(UL)
	merge_sort(LL)

	ULpoint = 0
	LLpoint = 0
	uind = 0
	while ULpoint < len(UL) and LLpoint < len(LL):
		if UL[ULpoint] < LL[LLpoint]:
			u[uind] = UL[ULpoint]
			ULpoint += 1
		else:
			u[uind] = LL[LLpoint]
			LLpoint += 1
		uind += 1
	while ULpoint < len(UL):
		u[uind] = UL[ULpoint]
		ULpoint += 1
		uind += 1
	while LLpoint < len(LL):
		u[uind] = LL[LLpoint]
		LLpoint += 1
		uind += 1
	return True

#v1=[10,9,8,7,6,5,4,3,2,1,0]
#v2=[100,1,1000,9,8,7,2,2000,10]
#v3=[100,10,1000,9,8,7,2,6,5,2,3,1]

#for i in [ v1,v2,v3 ]:
#	x=list(i)
#	selection_sort(x)
#	print("selection")	
#	print(x)
#
#	x=list(i)
#	heapify(x)
#	print("heapify")
#	print(x)
#
#	x=list(i)
#	heap_sort(x)
#	print("heap_sort")
#	print(x)
#
#	x=list(i)
#	merge_sort(x)
#	print("merge_sort")
#	print(x)
