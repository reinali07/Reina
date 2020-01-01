from queue import *
class tree:
	def __init__(self,x):
		self.store = [x,[]]
	def clearSuccessor(self):
		(self.store)[1] = []
		return True
	def AddSuccessor(self,x):
		(self.store)[1] = (self.store)[1] + [x]
		return True
	def Print_DepthFirst(self):
		self.printhelp("")
		return True
	def printhelp(self,indent):
		print(indent+str(self.store[0]))
		if (self.store)[1] != []:
			for i in range(0,len((self.store)[1]),1):
				(((self.store)[1])[i]).printhelp(indent+"   ")
		return True
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
	def ConvertToBinaryTree(self):
		newroot = self.btconverthelp([])
		return newroot
	def btconverthelp(self,siblings):
		from binary_tree import binary_tree
		root = self.store[0]
		children = self.store[1]
		if children == []:
			leftrestchildren = []
			leftnode = []
		else:
			firstchild = children[0]
			if len(children) < 2:
				leftrestchildren = []
			else:
				leftrestchildren = children[1:]
			leftnode = firstchild.btconverthelp(leftrestchildren)
		if siblings == []:
			rightrestsiblings = []
			rightnode = []
		else:
			firstsibling = siblings[0]
			if len(siblings) < 2:
				rightrestsiblings = []
			else:
				rightrestsiblings = siblings[1:]
			rightnode = firstsibling.btconverthelp(rightrestsiblings)
		newroot = binary_tree(root)
		if leftnode != []:
			newroot.AddLeft(leftnode)
		if rightnode != []:
			newroot.AddRight(rightnode)
		return newroot

