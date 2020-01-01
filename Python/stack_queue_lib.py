#last in, first out structure
class stack:
	def __init__(self):
		self.x = []

	def push(self,value):
		self.x = self.x + [value]
		return True
	def pop(self):
		if len(self.x) == 0:
			return False
		else:
			result = self.x[len(self.x)-1]
			self.x = self.x[0:len(self.x)-1]
			return result

#first in first out
class queue:
	def __init__(self):
		self.x = []
		self.maximum = N
	def add(self,value):
		if len(self.x) == self.maximum:
			return False
		else:
			self.x = [value] + self.x
			return True
	def delete(self):
		if len(self.x) == 0:
			return False
		else:
			result = self.x[len(self.x)-1]
			self.x = self.x[0:len(self.x)-1]
			return result
