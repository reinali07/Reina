def abs(x):
	if x<0:
		x=-x
	return x
print(abs(-6))
print(abs(16))
print(abs(-12))
print(abs(7))
print(abs(0))


def sqrt(x,y):
	estimate = x/2
	while abs(estimate*estimate-x) > y:
		estimate = (estimate + x/estimate)/2
	return int(estimate)
print(sqrt(49,1))
print(sqrt(25,2))
print(sqrt(36,4))
print(sqrt(49,7))
print(sqrt(81,10))
