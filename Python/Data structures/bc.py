from stackLib import *

def bc(x):
	a = stack()
	for i in range(0,len(x),1):
		if (x[i] == '(') or (x[i] == '[') or (x[i] == '{'):
			a.push(x[i])
		if (x[i] == ')') or (x[i] == ']') or (x[i] == '}'):
			if a.get() != []:
				check = [a.pop(),x[i]]
				if (check != ['(',')']) and (check != ['{','}']) and (check != ['[',']']):
					return [False,i]
			else:
				return [False,i]
	if a.get() == []:
		return [True,-1]
	else:
		return [False,i]


