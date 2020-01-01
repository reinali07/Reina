class seqdetector():
	def __init__(self):
		self.answer = ["here","are","the","solutions","to","the","next","exam"]
		self.state = "NULL" #self.state = 0
	def evolve(self,word):
		if self.state == "NULL":
			self.state = 0
		if word == self.answer[self.state]:
			self.state += 1
		else:
			self.state = "NULL"
		if self.state == len(self.answer):
			self.state = "DETECTED"  #self.state = 0; return True
		if self.state == "DETECTED":
			self.state = "NULL"
			return True
		return False

