#tic tac toe game

def genBoard():
	board = []
	for i in range(0,9,1):
		board = board + [0]
	return board


def printBoard(T):
	board = []
	noError = True
	if type(T) == int: #make sure we have a list of integers
		return False
	elif type(T) == str:
		return False
	for i in T:
		if type(i) == str:
			return False
	if len(T) == 9:
		for i in range(0,len(T),1): #iterate through T
			if int(T[i]) == 0:
				board = board + [str(i)]  #if unoccupied, print the position
			elif int(T[i]) == 1:
				board = board + ["X"]
			elif int(T[i]) == 2:
				board = board + ["O"]
			else: #if there's a value that's not 0,1,2
				noError = False
				break
		if noError == True:
			lineNumber = 0
			lines = ["" ,"---|---|---", "","---|---|---" ,""]
			for i in range(0,7,3): #index 0, 3, and 6 (beginning of each row)
				lines[lineNumber] = " " + board[i] + " | " + board[i+1] + " | " + board[i+2]
				lineNumber = lineNumber + 2 #line number includes the lines ---|---|---
			for i in lines:
				print(i)
	else: #if T is not length 9
		noError = False
	return noError
	
def analyzeBoard(T):
	status = -1
	wins = [0,0,0]
	error = False
	if type(T) == int:  #make sure we have a list of integers
		status = -1
		return status
	elif type(T) == str:
		status = -1
		return status
	for i in T:
		if type(i) == str:
			status = -1
			return status
	xPlaces = 0
	oPlaces = 0
	for i in T:
		if int(i) == 1: #if there are too many xs or too many os
			xPlaces += 1
		elif int(i) == 2:
			oPlaces += 1
	if not ((xPlaces == oPlaces + 1) or (xPlaces == oPlaces) or (oPlaces == xPlaces + 1)):
		status = -1
		return status
	if len(T) == 9:
		for i in range(0,len(T),1):
			if not (int(T[i]) <= 2 and int(T[i]) >= 0):
				status = -1
				return status
	else:
		status = -1
		return status
	for i in range(1,3,1): #iterate through 1, 2 to check Xs and then Os
		for n in range(0,7,3): #check rows
			if (int(T[n]) == i and int(T[n+1]) == i and int(T[n+2]) == i):
				#status = i
				wins[i] += 1
				break
		for n in range(0,3,1): #check columns
			if (int(T[n]) == i and int(T[n+3]) == i and int(T[n+6]) == i):
				#status = i
				wins[i] += 1
				break
		if (int(T[0]) == i and int(T[4]) == i and int(T[8]) == i): #check diagonal 0,4,8
			#status = i
			wins[i] += 1
			break
		if (int(T[2]) == i and int(T[4]) == i and int(T[6]) == i): #check diagonal 2,4,6
			#status = i
			wins[i] += 1
			break
	if (wins[1] > wins[2] and wins[2] == 0): #check if there are too many wins
		status = 1
	elif (wins[2] > wins[1] and wins[1] == 0):
		status = 2
	elif (wins[1] == wins[2] and wins[1] == 0):
		for i in T:
			if i == 0:  #check if game is on-going (are there still unoccupied spaces)
				status = 0
				break
			elif i == 1 or i == 2:   #no unoccupied spaces and no wins = draw
				status = 3
	else:
		status = -1
	return status

