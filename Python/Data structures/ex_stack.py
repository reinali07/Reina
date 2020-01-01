class stack:
	def __init__(self):
		self.x = []
	def pop(self):
		self.x = self.x[0:len(self.x)-1]
		return True
	def push(self,a):
		self.x = self.x + [a]
		return True
	def length(self):
		return len(self.x)
	def getStack(self):
		return self.x
