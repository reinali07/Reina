def fib(n):
	if n == 2 or n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return fib(n-1) + fib(n-2)
def fibList(N):
	if N == 0:
		return [0]
	else:
		return fibList(N-1) + [fib(N)]

def fibSum(N):
	flist = list(fibList(N))
	if len(flist) == 0:
		return 0
	elif len(flist) == 1:
		return flist[0]
	else:
		return flist[N] + fibSum(N-1)
print(fibSum(5))

