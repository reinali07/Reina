def rule(val,L):
	sumList = list(L)
	theSum = compress(sumList)
	if val == 1:
		if ((theSum == 2) or (theSum == 3)):
			return 1
		else:
			return 0
	else:
		if theSum == 3:
			return 1
		else:
			return 0

def compress(L):
	if len(L) == 0:
		return 0
	elif len(L) == 1:
		return L[0]
	else:
		return L[0] + compress(L[1:len(L)])


