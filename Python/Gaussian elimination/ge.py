def forwardStep(m):
	matrix = list(m)
	leadingones = False
	for i in range(0,len(matrix),1):
		for x in range(0,len(matrix[0]),1):
			if matrix[i][x] != 0:
				old = matrix[0]
				matrix[0] = matrix[i]
				matrix[i] = old
				leadingones = True
				leadingpos = x
				break
		if leadingones == True:
			break
	if leadingones == False:
		return m
	for i in range(1,len(matrix),1):
		multiple = -1*matrix[i][0]/matrix[0][leadingpos]
		for x in range(0,len(matrix[i]),1):
			matrix[i][x] = matrix[i][x] + multiple*matrix[0][x]
	return matrix
def checkifzeros(m):
	for i in m:
		for x in i:
			if x != 0:
				return False
	return True

def getSubfw(m):
	submatrix = list(m)
	submatrix = submatrix[1:len(m)]
	for i in range(0,len(submatrix),1):
		submatrix[i] = submatrix[i][1:len(submatrix[i])]
	return submatrix

def getSubbw(m,row):
	submatrix = list(m)
	submatrix = submatrix[0:row]
	return submatrix

def restoreMatrixfw(m,subm):
	matrix = list(m)
	rows = len(matrix)-len(subm)
	cols = len(matrix[0]) - len(subm[0])
	for i in range(rows,len(matrix),1):
		for x in range(cols,len(matrix[0]),1):
			matrix[i][x] = subm[i-rows][x-cols]
	return matrix

def restoreMatrixbw(m,subm):
	matrix = list(m)
	for i in range(0,len(subm),1):
		matrix[i] = subm[i]
	return matrix

def ge_fw(m):
	if checkifzeros(m) == True:
		return m
	matrix = list(m)
	matrix = forwardStep(matrix)
	submatrix = getSubfw(matrix)
	while (len(submatrix) > 0) and (len(submatrix[0]) > 1):
		submatrix = forwardStep(submatrix)
		matrix = restoreMatrixfw(matrix,submatrix)
		submatrix = getSubfw(submatrix)
	return matrix

def getFirstNum(r):
	for i in range(0,len(r),1):
		if r[i] != 0:
			return i
	return -1

def normalizeRow(r):
	if checkifzeros([r]) == True:
		return r
	x = getFirstNum(r)
	lead = r[x]
	for i in range(0,len(r),1):
		r[i] = r[i]/lead
	return r

def backStep(m):
	matrix = list(m)
	nonZeroRow = 0
	nonZeroPos = 0
	for i in range(len(matrix)-1,-1,-1):
		x = getFirstNum(matrix[i])
		if x != -1:
			nonZeroRow = i
			nonZeroPos = x
			break
	matrix[nonZeroRow] = normalizeRow(matrix[nonZeroRow])
	for i in range(nonZeroRow-1,-1,-1):
		multiple = -1*matrix[i][nonZeroPos]
		for x in range(0,len(matrix[i]),1):
			matrix[i][x] = matrix[i][x] + multiple*matrix[nonZeroRow][x]
	return [matrix,nonZeroRow]

def ge_bw(m):
	if checkifzeros(m) == True:
		return m
	matrix = list(m)
	temp = backStep(matrix)
	matrix = temp[0]
	submatrix = getSubbw(matrix,temp[1])
	while (len(submatrix) > 0) and (len(submatrix[0]) > 1):
		temp = backStep(submatrix)
		submatrix = temp[0]
		matrix = restoreMatrixbw(matrix,submatrix)
		submatrix = getSubbw(submatrix,temp[1])
	for i in range(0,len(matrix),1):
		for x in range(0,len(matrix[0]),1):
			if matrix[i][x] == -0:
				matrix[i][x] = 0.0
	return matrix
	
