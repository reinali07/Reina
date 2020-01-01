#check if brackets in a math expression make sense

from ex_stack import *

def isOBrack(x):
	if (x == "{") or (x == "[") or (x == "("):
		return True
	else:
		return False

def isCBrack(x):
	if(x == "}") or (x == "]") or (x == ")"):
		return True
	else:
		return False 
def isClosed(x):
	circle = ["(",")"]
	square = ["[","]"]
	curly = ["{","}"]
	temp = x.getStack()
	temp = temp[len(temp)-2:len(temp)]
	if temp == circle or temp == square or temp == curly:
		return True

def brackCheck(x):
	accum = stack()
	for i in range(0,len(x),1):
		if isOBrack(x[i]):
			accum.push(x[i])
		elif isCBrack(x[i]):
			accum.push(x[i])
			if isClosed(accum):
				accum.pop()
				accum.pop()
			else:
				return False
	return True

x = "{[1+(a+b)]+[2+(c+d)]}"
print(brackCheck(x))
x = "{[1+(a+b))+[2+(c+d)]"
print(brackCheck(x))

