#simple 2 player tic tac toe game

from tttlib import *


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
	moveO = input("O move?")
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
