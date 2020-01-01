class queue:
	def __init__(self):
		self.x = []
	def inqueue(self,a):
		self.x = self.x + [a]
		return True
	def enqueue(self):
		self.x = self.x[1:len(self.x)]
		return True
	def getQueue(self):
		return self.x
