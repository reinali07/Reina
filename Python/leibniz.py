def LeibnizPi(n):
	divPi = 0
	i = 1
	even = False
	while i < n:
		if even == True:
			divPi = divPi + 1/(2*i+1)
			even = False
		elif even == False:
			divPi = divPi - 1/(2*i+1)
			even = True
		i = i + 1
	leibPi = 4*(divPi + 1)
	return leibPi
print(LeibnizPi(500))
terms = 0

def abs(x):
	if x<0:
		return -x
	else:
		return x

while abs(LeibnizPi(terms) - 3.14159265) > 0.01:
	terms = terms + 1
print(terms)
print(LeibnizPi(terms))
