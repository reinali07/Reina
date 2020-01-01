def fibo(n):
    if (n==0) or (n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
def fiboL(n):
	accum = []
	for i in range(0,n+1,1):
		accum += [fibo(i)]
	return accum
def redProduct(a,b):
	return a*b
def redSum(a,b):
	return a+b

#function as parameter
def reduce(func,n):
	toRed = list(fiboL(n))
	counter = len(toRed)
	for i in range(0,counter-1,1):
		toRed[i+1] = func(toRed[i],toRed[i+1])
	return toRed[len(toRed)-1]
def redfibo(n):
	return reduce(redProduct,n)


