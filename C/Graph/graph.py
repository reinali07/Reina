class queue:
	def __init__(self):
		self.store = []
	def add(self,x):
		self.store += [x]
		return True
	def remove(self):
		hold = self.store[0]
		self.store = self.store[1:]
		return hold
	def empty(self):
		if len(self.store) == 0:
			return True
		else:
			return False
class stack:
	def __init__(self):
		self.store = []
	def add(self,x):
		self.store += [x]
		return True
	def remove(self):
		hold = self.store[-1]
		self.store = self.store[0:-1]
		return hold
	def empty(self):
		if len(self.store) == 0:
			return True
		else:
			return False
class tree:
	def __init__(self,x):
		self.store = [x,[]]
		self.parent = None
		self.root = self
	def clearSuccessor(self):
		(self.store)[1] = []
		return True
	def AddSuccessor(self,x):
		(self.store)[1] = (self.store)[1] + [x]
		x.parent = self
		x.root = self.root
		return True
	def Get_DepthFirst(self):
		accum = []
		nebu = stack()
		nebu.add(self.store)
		while nebu.empty() == False:
			y = nebu.remove()
			accum = accum + [y[0]]
			for i in y[1]:
				nebu.add(i.store)
		return accum
	def Get_Trees(self):
		accum = []
		nebu = stack()
		nebu.add(self.store)
		while nebu.empty() == False:
			y = nebu.remove()
			accum = accum + [y[0]]
			for i in y[1]:
				nebu.add([i] + [i.store[1]])
		return accum
	def Get_LevelOrder(self):
		accum = []
		nebu = queue()
		nebu.add(self.store)
		while nebu.empty() == False:
			y = nebu.remove()
			accum = accum + [y[0]]
			for i in y[1]:
				nebu.add(i.store)
		return accum
	def Print_DepthFirst(self):
		self.printhelp("")
		return True
	def printhelp(self,indent):
		print(indent+str(self.store[0]))
		if (self.store)[1] != []:
			for i in range(0,len((self.store)[1]),1):
				(((self.store)[1])[i]).printhelp(indent+"   ")
		return True
	def getParents(self):
		accum = []
		accum = [self.store[0]] + self.parenthelp(accum)
		return accum
	def parenthelp(self,x):
		accum = list(x)
		if self.parent != None:
			accum += [(self.parent).store[0]]
			accum = (self.parent).parenthelp(accum)
		return accum
class graph:
	def __init__(self):
		self.adj = []
		self.vals = []
	def addVertex(self,n):
		for i in range(0,n,1):
			self.adj += [[]]
		return len(self.adj)
	def addEdge(self,from_idx,to_idx,directed,weight):
		if from_idx >= len(self.adj) or to_idx >= len(self.adj) or weight == 0 or directed != False and directed != True:
			return False
		for i in self.adj[from_idx]:
			if i[0]==to_idx:
				return False
		self.adj[from_idx] += [[to_idx,weight]]
		if directed != True:
			for i in self.adj[to_idx]:
				if i[0] == from_idx:
					return False
			self.adj[to_idx] += [[from_idx,weight]]
		return True
	def traverse(self,start,typeBreadth):
		accum = []
		if typeBreadth == True:
			C = queue()
		else:
			C = stack()
		Discovered = len(self.adj)*[False]
		Processed = len(self.adj)*[False]
		if start == None:
			vertices = self.adj
			begin = 0
		else:
			vertices = self.adj[start:]
			begin = start
		for i in range(begin,len(self.adj),1):
			island = []
			if Discovered[i] == False:
				C.add(i)
				Discovered[i] = True
			while C.empty() == False:
				#print("accum is " + str(accum))
				#print("C.store is " + str(C.store))
				w = C.remove()
				#print("w is " + str(w))
				if Processed[w] == False:
					#print(self.vals[w])
					island += [w]
					Processed[w] = True
				#print("adj of w is " + str(self.adj[w]))
				for j in self.adj[w]:
					#print("j is " + str(j))
					x = j[0]
					#print(x)
					if Discovered[x] == False:
						C.add(x)
						Discovered[x] = True
			if island != []:
				accum += [island]
		#print(accum)
		if start == None:
			return accum
		else:
			return accum[0]
	def connectivity(self,vx,vy):
		x2y = self.traverse(vx,False)
		xy = False
		for i in x2y:
			if i == vy:
				xy = True
		y2x = self.traverse(vy,False)
		yx = False
		for i in y2x:
			if i == vx:
				yx = True
		return [xy,yx]
	def maketree(self,node,vy):
		discovered = (node.root).Get_LevelOrder()
		#print(discovered)
		vx = node.store[0]
		connected = []
		foundvy = False
		for i in self.adj[vx]:
			connected += [i[0]]
		#print("node is " + str(node.store[0]))
		#print("connected is " + str(connected))
		for i in connected:
			found = False
			for j in discovered:
		#		print("j is " + str(j) + " and i is " + str(i))
				if i == j:
					found = True
					break
		#	print(found)
			if found == False:
				if i == vy:
					foundvy = True
				node.AddSuccessor(tree(i))
		#node.Print_DepthFirst()
		if foundvy == False:
			for i in node.store[1]:
				self.maketree(i,vy)
		return True
	def path_Directed(self,vx,vy):
		#### x to y ####
		root = tree(vx)
		self.maketree(root,vy)
		#root.Print_DepthFirst()
		found = False
		depthfirst = root.Get_DepthFirst()
		#print(depthfirst)
		for i in range(0,len(depthfirst),1):
			if depthfirst[i] == vy:
				found = True
		#		print("i is " + str(i))
				break
		node = root.Get_Trees()[i]
		accum = node.getParents()
		path = []
		for i in range(len(accum)-1,-1,-1):
			path += [accum[i]]
		#print(path)
		return path
	def path(self,vx,vy):
		nodeconnectivity = self.connectivity(vx,vy)
		if nodeconnectivity[0] == True:
			vx_vy = self.path_Directed(vx,vy)
		else:
			vx_vy = []
		if nodeconnectivity[1] == True:
			vy_vx = self.path_Directed(vy,vx)
		else:
			vy_vx = []
		return [vx_vy,vy_vx]
