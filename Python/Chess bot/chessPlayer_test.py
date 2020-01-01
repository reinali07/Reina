from time import time
from chessPlayer import *
def main():
    board = genBoard()
    timea = 0
    timeb = 0
    for j in range(0,30,1):
        start = time()
        move = chessPlayer(board,10)
        print(move)
        board = makeMove(board,move[1][0],move[1][1])
        end = time()
        print(end-start)
        timea = max(timea,end-start)
        print("after white")
        printboard(board)
        #input("enter")
        start = time()
        move = chessPlayer(board,20)
        board = makeMove(board,move[1][0],move[1][1])
        end = time()
        print(end-start)
        timeb = max(timeb,end-start)
        print("after black")
        printboard(board)
    printboard(board)
    print(timea)
    print(timeb)
    print(evalBoardEnd(board,10))
main()

