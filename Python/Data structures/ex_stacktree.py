class Stack:
	def __init__(self):
		self.x = []
	def push(self,T):
		self.x = self.x + [T]
		return True
	def pop(self):
		save = (self.x)[len(self.x)-1]
		self.x = (self.x)[0:len(self.x)-1]
		return save
	def empty(self):
		if self.x == []:
			return True
		else:
			return False

def traverse_breadth(T):
	x=Stack()
	x.push(T)
	while x.empty() == False:
		r = x.pop()
		print(r[0])
		for i in r[1:len(r)]:
			x.push(i)

traverse_breadth([[1],[[2],[[3],[4],[5],[6]],[7]],[[8],[[9],[[10],[[11],[12]],[13]]]]])

