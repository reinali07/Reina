def Palindromize(string):
	i = 0
	strList = []
	while i < len(string):
		strList = strList + [string[i]]
		i = i + 1
	toFlip = strList[0:len(strList)-1]
	i = len(toFlip)-1
	while i >= 0:
		strList = strList + [toFlip[i]]
		i = i - 1
	palinString = ""
	for i in strList:
		palinString = palinString + i
	return palinString

print(Palindromize("abc"))
print(Palindromize("this is an exercise"))
print(Palindromize("i"))
print(Palindromize(""))
