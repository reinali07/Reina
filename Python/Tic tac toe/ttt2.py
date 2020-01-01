#for a simple tic tac toe bot

from tttlib import *
import random

def blockWin(T):
	rows = []
	for i in range(0,len(T),3):
		rows = rows + [int(T[i]),int(T[i+1]), int(T[i+2])]
	columns = []
	for i in range(0,len(T),1):
		columns = columns + [int(T[i]),int(T[i+3]),int(T[i+6])]
	diagonals = [[int(T[0]),int(T[4]),int(T[8])],[int(T[2]),int(T[4]),int(T[6])]]
	for i in range(0,len(rows),1):
		xCount = 0
		noneCount = 0
		nonePos = False
		for n in range(0,len(columns[i]),1):
			if rows[i][n] == 0:
				noneCount += 1
				nonePos = n
			elif rows[i][n] == 1:
				xCount += 1
		if (noneCount == 1 and xCount == 2):
			return i + nonePos
	for i in range(0,len{columns),1):
		xCount = 0
                noneCount = 0
                nonePos = False
                for n in range(0,len(columns[i]),1):
                        if columns[i][n] == 0:
                                noneCount += 1
                                nonePos = n
                        elif columns[i][n] == 1:
                                xCount += 1
                if (noneCount == 1 and xCount == 2):
                        return 

def unoccupied(T):
	unoccupied = []
	for i in range(0,len(T),1):
		if int(T[i]) == 0:
			unoccupied = unoccupied + [i]
	return unoccupied

def findX(T):
	xPos = []
	for i in range(0,len(T),1):
		if int(T[i]) == 1:
			xPos = xPos + [i]
	return xPos

#def winMove(T):
	

def nonLoseMove(T):
	unoccupied = unoccupied(T)
	xMoves = findX(T)
	if len(xMoves) == 1:
		if (xMoves[0] == 0 or xMoves[0] == 2 or xMoves[0] ==  6 or xMoves[0] == 8):
			return 4
		



def randomMove(T):
	unoccupied = unoccupied(T)
	move = random.randint(0,len(unoccupied)-1)
	return unoccupied[move]


T = genBoard()
while True:
	printBoard(T)
	moveX = input("X move?")
	if (int(moveX) >= 0 and int(moveX) <= 8 and T[int(moveX)] == 0):
		T[int(moveX)] = 1
	else:
		break
	state = analyzeBoard(T)
	if state == 1:
		printBoard(T)
		print("X won")
		break
	elif state == 3:
		printBoard(T)
		print("It's a draw")
		break
	printBoard(T)
	moveO = randomMove(T)
	print("O move")
	if (int(moveX) >= 0 and int(moveX) <= 8 and T[int(moveO)] == 0):
		T[int(moveO)] = 2
	else:
		break
	state = analyzeBoard(T)
	if state == 2:
		printBoard(T)
		print("O won")
		break
	elif state == 3:
		printBoard(T)
		print("It's a draw")
		break
