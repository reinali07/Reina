class stack:
	def __init__(self):
		self.x = []
	def push(self,value):
		self.x = self.x + [value]
		return True
	def pop(self):
		if self.x == []:
			return False
		return_val = self.x[len(self.x)-1]
		self.x = (self.x)[0:len(self.x)-1]
		return return_val
	def get(self):
		return self.x
