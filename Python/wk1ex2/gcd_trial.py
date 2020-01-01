def gcd(x,y):
	if x<y:
		lesser = x
	else:
		lesser = y
	i = lesser
	while i > 0:
		if is_factor(i,x) and is_factor(i,y):
			break
		else:
			i=i-1
	return i


def is_factor(factor,multiple):
	i = 0
	is_factor = False
	while i < multiple:
		if factor*i == multiple:
			is_factor = True
			break
		else:
			i=i+1
	return is_factor

print(is_factor(4,6))
print(gcd(30,25))
'''
