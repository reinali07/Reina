from ge import *

m = [[5,3,7,2,7],[4,2,7,4,6],[1,0,3,5,3],[8,7,8,0,3],[0,1,1,2,3],[0,6,4,1,2]]

m = ge_fw(m)
m = ge_bw(m)
for i in m:
	print(i)
print("")
n = [[1,1]]
n = ge_fw(n)
n = ge_bw(n)
for i in n:
	print(i)
print("")
n = [[1],[2]]
n = ge_fw(n)
n = ge_bw(n)
for i in n:
        print(i)
print("")
n = [[1,1,1,1],[0,2,4,1],[1,1,2,3],[6,2,4,6]]
n = ge_fw(n)
n = ge_bw(n)
for i in n:
        print(i)
print("")
n = [[1,10,4,6],[3,1,2,4],[5,0,0,1]]
n = ge_fw(n)
n = ge_bw(n)
for i in n:
        print(i)
print("")
n = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
n = ge_fw(n)
n = ge_bw(n)
for i in n:
        print(i)
print("")
n = [[0,0,0,0],[0,0,0,0],[0,0,0,1]]
n = ge_fw(n)
n = ge_bw(n)
for i in n:
        print(i)
