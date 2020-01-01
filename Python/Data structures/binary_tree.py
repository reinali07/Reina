from queue import *
class binary_tree:
	def __init__(self,val):
		self.store = [val]
	def AddLeft(self,x):
		if len(self.store) == 1:
			self.store = self.store + [x,None]
		elif self.store[1] == None:
			self.store[1] = x
		else:
			return False
		return True
	def AddRight(self,x):
		if len(self.store) == 1:
			self.store = self.store + [None,x]
		elif self.store[2] == None:
			self.store[2] = x
		else:
			return False
		return True
	def Get_LevelOrder(self):
		nebu = queue()
		accum = []
		filtered = []
		nebu.enqueue(self.store)
		while True:
			y = nebu.dequeue()
			if y[0] == False:
				break
			else:
				accum = accum + [y[1][0]]
				for i in y[1][1:]:
					if type(i) == binary_tree:
						nebu.enqueue(i.store)
					else:
						nebu.enqueue([i])
		for i in accum:
			if i != None:
				filtered = filtered + [i]
		return filtered
	def getSuccessors(self):
		return self.store[1:]
	def getRight(self):
		if len(self.store) != 1:
			if self.store[2] != None:
				return self.store[2]
		return False
	def getRightBranch(self):
		accum = [self]
		point = self
		while True:
			if point.getRight() != False:
				accum = accum + [point.getRight()]
				point = point.getRight()
			else:
				break
		return accum
	def Print_DepthFirst(self):
		self.printhelp("")
		return True
	def printhelp(self,indent):
		print(indent+str(self.store[0]))
		if len(self.store) != 1 and (self.store[1] != None or self.store[2] != None):
			for i in range(0,len((self.store)[1:]),1):
				if ((self.store)[1:])[i] != None:
					(((self.store)[1:])[i]).printhelp(indent+"   ")
		return True
	def getLeft(self):
		if self.store[1] != None:
			return self.store[1]
		else:
			return False
	def ConvertToTree(self):
		if self.store[2] == None:
			return [True,self.converthelper()]
		else:
			return [False,None]
	def converthelper(self):
		from tree import tree
		leftchild = self.store[1]
		newroot = tree(self.store[0])
		successors = leftchild.getRightBranch()
		if len(leftchild.store) != 1:
			grandchild = leftchild.store[1]
		else:
			grandchild = None
		if grandchild != None:
			leftchild = leftchild.converthelper()
			newroot.AddSuccessor(leftchild)
		else:
			leftchild = tree(leftchild.store[0])
			newroot.AddSuccessor(leftchild)
		for i in range(1,len(successors),1):
			if len(successors[i].store) != 1 and (successors[i]).store[1] != None:
				(successors[i]) = (successors[i]).converthelper()
			else:
				(successors[i]) = tree(successors[i].store[0])
		for i in successors[1:]:
			newroot.AddSuccessor(i)	
		return newroot
