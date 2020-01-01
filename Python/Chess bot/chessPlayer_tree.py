from random import shuffle
from random import random
from random import randint
from chessPlayer_queue import queue
class minimax:
    def __init__(self,x,score,player,depth): #x is the board
        self.store = [x,[]]
        self.score = score
        self.player = player
        if player == 10:
            self.max = 1
            self.opp = 20
        elif player == 20:
            self.max = -1
            self.opp = 10
        self.depth = depth
    def clearSuccessor(self):
        (self.store)[1] = []
        return True
    def AddSuccessor(self,x):
        if x.player != self.player:
            return False
        (self.store)[1] = (self.store)[1] + [x]
        return True
    def Print_DepthFirst(self):
        self.printhelp("")
        return True
    def printhelp(self,indent):
        printboard(self.store[0])
        #print(indent + str((self.store)[0]))
        if (self.store)[1] != []:
            for i in range(0,len((self.store)[1]),1):
                        (((self.store)[1])[i]).printhelp(indent+"    ")
        return True
    def populate(self):
        self.populatehelp(0,True)
        return True
    def populatehelp(self,depth,pm):
        from chessPlayer import GetPlayerPositions
        from chessPlayer import GetPieceLegalMoves
        from chessPlayer import makeMove
        from chessPlayer import evalBoard
        playermove = pm
        if playermove == True:
            player = self.player
            playermove = False
        else:
            player = self.opp
            playermove = True
        if depth <= self.depth:
            if (self.store)[1] == []:
                moves = []
                pieces = GetPlayerPositions(self.store[0],player)
                shuffle(pieces)
                for i in range(0,len(pieces),1):
                    possiblemoves = GetPieceLegalMoves(self.store[0],pieces[i])
                    shuffle(possiblemoves)
                    for j in range(0,len(possiblemoves),1):
                        if (j+1)%5!=0 and (self.store[0])[possiblemoves[j]] != 25 and (self.store[0])[possiblemoves[j]] != 15:
                            moves += [makeMove(self.store[0],pieces[i],possiblemoves[j])]
                    shuffle(moves)
                for i in range(0,len(moves),1):
                    self.AddSuccessor(minimax(moves[i],evalBoard(moves[i],self.player),self.player,self.depth))
            for i in range(0,len((self.store)[1]),1):
                (((self.store)[1])[i]).populatehelp(depth+1,playermove)
        return True
    def alphabeta(self):
        infinity = float('inf')
        bestVal = -infinity
        beta = infinity
        successors = self.store[1]
        bestState = None
        for state in successors:
            value = state.min_value(bestVal,beta)
            if value > bestVal:
                bestVal = value
                bestState = state
        return bestState
    def max_value(self,alpha,beta):
        if self.store[1] == []:
            return self.score
        infinity = float('inf')
        value = -infinity
        successors = self.store[1]
        for state in successors:
            value = max(value,state.min_value(alpha,beta))
            if value >= beta:
                return value
            alpha = max(alpha,value)
        return value
    def min_value(self,alpha,beta):
        if self.store[1] == []:
            return self.score
        infinity = float('inf')
        value = infinity
        successors = self.store[1]
        for state in successors:
            value = min(value,state.max_value(alpha,beta))
            if value <= alpha:
                return value
            beta = min(beta,value)
        return value
    def Get_LevelOrder(self):
        accum = []
        nebu = queue()
        nebu.enqueue(self.store)
        while True:
            y = nebu.dequeue()
            if y[0] == False:
                break
            else:
                v=y[1]
                accum = accum + [v[0]]
                for i in v[1]:
                    nebu.enqueue(i.store)
        return accum
