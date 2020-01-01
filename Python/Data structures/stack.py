class stack:
	def __init__(self):
		self.store = []
	def push(self,x):
		self.store = self.store + [x]
		return True
	def pop(self):
		save = (self.store)[len(self.store)-1]
		self.store = (self.store)[0:len(self.store)-1]
		return save
	def empty(self):
		if len(self.store) == 0:
			return True
		else:
			return False
