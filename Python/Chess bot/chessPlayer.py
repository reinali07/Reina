from random import shuffle
from random import random
from random import randint
def compare(old,new):
    start = -1
    end = -1
    for i in range(0,len(old),1):
        if new[i] == 0 and old[i] != 0:
            start = i
    for i in range(0,len(old),1):
        if new[i] != old[i] and new[i] != 0:
            end = i
    if start != -1 and end != -1:
        return [start,end]
    else:
        return False
def GetPlayerPositions(board,player):
    accum = []
    for i in range(0,len(board),1):
        if board[i]/player < 2 and board[i]/player >= 1:
            accum += [i]
    return accum
def isTeam(board,player,position):
    if board[position]/player < 2 and board[position]/player >= 1:
        return True
    else:
        return False
def isOpp(board,player,position):
    if player == 10:
        opponent = 20
    elif player == 20:
        opponent = 10
    if board[position]/opponent < 2 and board[position]/opponent >= 1:
        return True
    else:
        return False

def isOnBoard(board,position):
    if position >= 0 and position <= 63:
        return True
    else:
        return False
def getPawnMoves(board,player,position):
    accum = []
    if player == 10:
        forward = 1
        opponent = 20
    elif player == 20:
        forward = -1
        opponent = 10
    else:
        return False
    leftspaces = position%8
    rightspaces = 7 - (position%8)
    if isOnBoard(board,position+forward*8)== True:
        if (isTeam(board,player,position+forward*8) == False) and (isOpp(board,player,position+forward*8) == False):
            accum += [position+forward*8]
        if leftspaces >= 1 and isOpp(board,player,position+7) and forward == 1:
            accum += [position+7]
        if leftspaces >= 1 and isOpp(board,player,position-9) and forward == -1:
            accum += [position-9]
        if rightspaces >= 1 and isOpp(board,player,position+9) and forward == 1:
            accum += [position+9]
        if rightspaces >= 1 and isOpp(board,player,position-7) and forward == -1:
            accum += [position-7]
    return accum
def getBishopMoves(board,player,position):
    accum = []
    leftspaces = position%8
    rightspaces = 7 - (position%8)
    frontleft = position
    frontright = position
    backleft = position
    backright = position
    for i in range(0,leftspaces,1):
        frontleft += 7
        if isOnBoard(board,frontleft):
            if isTeam(board,player,frontleft) == True:
                break
            accum += [frontleft]
            if isOpp(board,player,frontleft) == True:
                break
    for i in range(0,leftspaces,1):
        backleft -= 9
        if isOnBoard(board,backleft):
            if isTeam(board,player,backleft) == True:
                break
            accum += [backleft]
            if isOpp(board,player,backleft) == True:
                break
    for i in range(0,rightspaces,1):
        frontright += 9
        if isOnBoard(board,frontright):
            if isTeam(board,player,frontright) == True:
                break
            accum += [frontright]
            if isOpp(board,player,frontright) == True:
                break
    for i in range(0,rightspaces,1):
        backright -= 7
        if isOnBoard(board,backright):
            if isTeam(board,player,backright) == True:
                break
            accum += [backright]
            if isOpp(board,player,backright) == True:
                break
    return accum
def getRookMoves(board,player,position):
    accum = []
    leftspaces = position%8
    rightspaces = 7 - (position%8)
    front = position
    back = position
    left = position
    right = position
    while isOnBoard(board,front):
        front += 8
        if isOnBoard(board,front):
            if isTeam(board,player,front) == True:
                break
            accum += [front]
            if isOpp(board,player,front) == True:
                break
    while isOnBoard(board,back):
        back -= 8
        if isOnBoard(board,back):
            if isTeam(board,player,back) == True:
                break
            accum += [back]
            if isOpp(board,player,back) == True:
                break
    for i in range(0,leftspaces,1):
        left -= 1
        if isOnBoard(board,left):
            if isTeam(board,player,left) == True:
                break
            accum += [left]
            if isOpp(board,player,left) == True:
                break
    for i in range(0,rightspaces,1):
        right += 1
        if isOnBoard(board,right):
            if isTeam(board,player,right) == True:
                break
            accum += [right]
            if isOpp(board,player,right) == True:
                break
    return accum
def getKnightMoves(board,player,position):
    accum = []
    leftspaces = position%8
    rightspaces = 7 - (position%8)
    if leftspaces >= 2:
        if isOnBoard(board,position+6) and isTeam(board,player,position+6) == False:
            accum += [position+6]
        if isOnBoard(board,position-10) and isTeam(board,player,position-10) == False:
            accum += [position-10]
    if leftspaces >= 1:
        if isOnBoard(board,position+15) and isTeam(board,player,position+15) == False:
            accum += [position+15]
        if isOnBoard(board,position-17) and isTeam(board,player,position-17) == False:
            accum += [position-17]
    if rightspaces >= 2:
        if isOnBoard(board,position+10) and isTeam(board,player,position+10) == False:
            accum += [position+10]
        if isOnBoard(board,position-6) and isTeam(board,player,position-6) == False:
            accum += [position-6]
    if rightspaces >= 1:
        if isOnBoard(board,position+17) and isTeam(board,player,position+17) == False:
            accum += [position+17]
        if isOnBoard(board,position-15) and isTeam(board,player,position-15) == False:
            accum += [position-15]
    return accum
def GetPieceLegalMoves(board,position):
    piece = board[position]%10
    if board[position] < 20 and board[position] >= 10:
        player = 10
    elif board[position] >= 20:
        player = 20
    else:
        return []
    if piece == 0: #pawn
        return getPawnMoves(board,player,position)
    elif piece == 1: #knight
        return getKnightMoves(board,player,position)
    elif piece == 2: #bishop
        return getBishopMoves(board,player,position)
    elif piece == 3: #rook
        return getRookMoves(board,player,position)
    elif piece == 4: #queen
        return getBishopMoves(board,player,position) + getRookMoves(board,player,position)
    elif piece == 5: #king
        accum = []
        queen = getBishopMoves(board,player,position) + getRookMoves(board,player,position)
        for i in queen:
            if i == position + 7 or i == position + 8 or i == position + 9 or i == position -1 or i == position + 1 or i == position - 8 or i == position - 9 or i == position - 7:
                accum += [i]
        return accum
def IsPositionUnderThreat(board,position,player):
    if player == 10:
        opponent = 20
    elif player == 20:
        opponent = 10
    else:
        return False
    opos = GetPlayerPositions(board,opponent)
    for i in opos:
        moves = GetPieceLegalMoves(board,i)
        for x in moves:
            if x == position:
                return True
    return False
def isCheck(board,player):
    if player == 10:
        king = 15
    elif player == 20:
        king = 25
    else:
        return False
    for i in range(0,len(board),1):
        if board[i] == king:
            break
    return IsPositionUnderThreat(board,i,player)
def printboard(board):
   accum=""
   max=63
   for i in range(0,8,1):
      for x in range(max-i*8-7,max-i*8+1,1):
         accum=accum+'{0: <5}'.format(str(board[x]))
      accum=accum+"\n"
   print(accum)
   return True
def makeMove(board,piece,move):
    newboard = list(board)
    if piece != move:
        newboard[move] = newboard[piece]
        newboard[piece] = 0
    return newboard
def evalBoard(board,player):
    accum = 0
    if isCheck(board,player):
        accum -= 900
    if player == 10:
        for i in board:
            if i == 20:
                accum += -10
            elif i == 21 or i == 22:
                accum += -30
            elif i == 23:
                accum += -50
            elif i == 24:
                accum += -90
            elif i == 25:
                accum += -900
            elif i == 10:
                accum += 10
            elif i == 11 or i == 12:
                accum += 30
            elif i == 13:
                accum += 50
            elif i == 14:
                accum += 90
            elif i == 15:
                accum += 900
    elif player == 20:
        for i in board:
            if i == 20:
                accum += 10
            elif i == 21 or i == 22:
                accum += 30
            elif i == 23:
                accum += 50
            elif i == 24:
                accum += 90
            elif i == 25:
                accum += 900
            elif i == 10:
                accum += -10
            elif i == 11 or i == 12:
                accum += -30
            elif i == 13:
                accum += -50
            elif i == 14:
                accum += -90
            elif i == 15:
                accum += -900
    return accum
def evalBoardEnd(board,player):
    accum = 0
    if player == 10:
        for i in board:
            if i == 20:
                accum += -10
            elif i == 21 or i == 22:
                accum += -30
            elif i == 23:
                accum += -50
            elif i == 24:
                accum += -90
            elif i == 25:
                accum += -900
            elif i == 10:
                accum += 10
            elif i == 11 or i == 12:
                accum += 30
            elif i == 13:
                accum += 50
            elif i == 14:
                accum += 90
            elif i == 15:
                accum += 900
    elif player == 20:
        for i in board:
            if i == 20:
                accum += 10
            elif i == 21 or i == 22:
                accum += 30
            elif i == 23:
                accum += 50
            elif i == 24:
                accum += 90
            elif i == 25:
                accum += 900
            elif i == 10:
                accum += -10
            elif i == 11 or i == 12:
                accum += -30
            elif i == 13:
                accum += -50
            elif i == 14:
                accum += -90
            elif i == 15:
                accum += -900
    return accum
def genBoard():
    board = [13,11,12,14,15,12,11,13]
    for i in range(0,8,1):
        board += [10]
    for i in range(0,8*4,1):
        board += [0]
    for i in range(0,8,1):
        board += [20]
    board += [23,21,22,24,25,22,21,23]
    return board
def chessPlayer(board,player):
    from chessPlayer_tree import minimax
    evtree = minimax(board,0,player,2)
    evtree.populate()
    status = True
    bestState = evtree.alphabeta()
    move = []
    candidatemoves = []
    levelorder = []
    if bestState == None:
        status = False
    if status == True:
        move = compare(board,bestState.store[0])
        for i in GetPlayerPositions(board,player):
            for j in GetPieceLegalMoves(board,i):
                candidatemoves += [[[i,j],random()]]
                levelorder += [[i,j]]
        for i in candidatemoves:
            if i[0] == move:
                i[1] = 1
    return [status,move,candidatemoves,levelorder]
