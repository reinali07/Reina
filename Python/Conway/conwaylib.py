import random
from rule import *
class conway:
	def __init__(self,row,col,instruct):
		self.store = []
		self.rows = row
		self.cols = col
		oneRow = []
		if instruct == 'zeros':
			for i in range(0,row,1):
				oneRow = []
				for i in range(0,col,1):
					oneRow += [0]
				self.store += [oneRow]
		elif instruct == 'random':
			for i in range(0,row,1):
				oneRow = []
				for i in range(0,col,1):
					oneRow += [random.randint(0,1)]
				self.store += [oneRow]
	def getDisp(self):
		accum = ""
		for i in range(0,len(self.store),1):
			for x in range(0,len(self.store[i]),1):
				if (self.store[i])[x] == 0:
					accum += " "
				elif (self.store[i])[x] == 1:
					accum += "*"
			accum += "\n"
		return accum
	def printDisp(self):
		toPrint = str(self.getDisp())
		listToPrint = toPrint.split('\n')
		for i in listToPrint:
			print(i)
		return True
	def setPos(self,theRow,theCol,val):
		if not((str(val) == "0") or (str(val) == "1")):
			return False
		else:
			(self.store[theRow])[theCol] = val
			return True
	def getNeighbours(self,aRow,aCol):
		if (aRow >= len(self.store)) or (aCol >= len(self.store[0])):
			return False
		if aCol == 0:
			left = len(self.store[0]) - 1
			right = aCol + 1
		elif aCol == len(self.store[0])-1:
			left = aCol - 1
			right = 0
		else:
			left = aCol - 1
			right = aCol + 1
		if aRow == 0:
			up = len(self.store)-1
			down = aRow + 1
		elif aRow == len(self.store)-1:
			up = aRow - 1
			down = 0
		else:
			up = aRow - 1
			down = aRow + 1
		accum = []
		rows = [up,aRow,down]
		columns = [left, aCol, right]
		count = 0
		for i in range(0,len(rows),1):
			for x in range(0,len(columns),1):
				if count != 4:
					accum += [self.store[rows[i]][columns[x]]]
				count += 1
		return accum
	def evolve(self,rule):
		nextState = conway(self.rows,self.cols,'zeros')
		#nextState.printDisp()
		for n in range(0,self.rows,1):
			for t in range(0,self.cols,1):
				#self.printDisp()
				#print("row:",str(n),"col:",str(t))
				#print(self.getNeighbours(n,t))
				#print(self.store[n][t])
				#print(compress(self.getNeighbours(n,t)))
				value = rule((self.store[n])[t],self.getNeighbours(n,t))
				#print(value)
				nextState.setPos(n,t,value)
		self.store = nextState.store
		return True


