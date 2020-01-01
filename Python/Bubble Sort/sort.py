def bubbleSort(array):
	n = len(array)
	rval = list(array)
	if n == 0:
		status = False
		return [status, rval]
	swapped = True
	while swapped == True:
		swapped = False
		for i in range(1,n,1):
			if rval[i-1] > rval[i]:
				old = rval[i]
				rval[i] = rval[i-1]
				rval[i-1] = old
				swapped = True
	status = True
	return [status, rval]
