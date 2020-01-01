def gcd(x,y):
	while not x==y:
		if x>y:
			x = x-y
		else:
			y = y-x
	return x
print(gcd(18,12))
print(gcd(8,12))
print(gcd(24,12))
print(gcd(35,30))
print(gcd(72,49))
print(gcd(18,30))
