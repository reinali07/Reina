def isBlah(n):
    for i in range(3,n,2):
    	if n%i == 0:
    		return True
    return False

#list of first n composite numbers with odd divisors
def blahList(n):
    i = 0
    accum = []
    while len(accum) < n:
        if isBlah(i) == True:
            accum = accum + [i]
        i = i + 1
    return accum
print(blahList(10))

#basel series
def srs(n):
    sum = 0
    for i in range(1,n+1,1):
        sum += float(1/(i*i))
    return sum
print(srs(10000))

#converts sentence into list of words 
def str2LoW(words):
    accum = []
    lastspacei = 0
    for i in range(0,len(words),1):
        if words[i] == " ":
            accum = accum + [words[lastspacei:i]]
            lastspacei = i+1
    accum = accum + [words[lastspacei:len(words)]]
    return accum
print(str2LoW("this is a sample string"))
