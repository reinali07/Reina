from tree import *
from binary_tree import *
x=tree(1)
y=tree(2)
z=tree(3)
j=tree(4)
d=tree(5)
e=tree(6)
c=tree(7)
o=tree(8)
p=tree(9)
q=tree(10)
f=tree(11)
g=tree(12)
h=tree(13)
i=tree(14)
k=tree(15)
l=tree(16)
m=tree(17)
n=tree(18)
x.AddSuccessor(y)
x.AddSuccessor(z)
x.AddSuccessor(j)
y.AddSuccessor(d)
y.AddSuccessor(e)
z.AddSuccessor(c)
j.AddSuccessor(o)
j.AddSuccessor(p)
j.AddSuccessor(q)
d.AddSuccessor(f)
d.AddSuccessor(g)
d.AddSuccessor(h)
h.AddSuccessor(i)
h.AddSuccessor(k)
k.AddSuccessor(l)
k.AddSuccessor(m)
k.AddSuccessor(n)

x.Print_DepthFirst()
print(x.Get_LevelOrder())

binary = x.ConvertToBinaryTree()
binary.Print_DepthFirst()
print(binary.Get_LevelOrder())
general = (binary.ConvertToTree())[1]
if general != None:
	general.Print_DepthFirst()
	print(general.Get_LevelOrder())
else:
	print("cannot be converted")

x1=binary_tree(1)
y1=binary_tree(2)
z1=binary_tree(3)
x1.AddLeft(y1)
x1.AddRight(z1)
x1.Print_DepthFirst()
print(x1.Get_LevelOrder())
general1 = (x1.ConvertToTree())[1]
if general1 != None:
	general1.Print_DepthFirst()
else:
	print("cannot be converted")

x2=tree(1)
y2=tree(2)
z2=tree(3)
j2=tree(4)
d2=tree(5)
e2=tree(6)
c2=tree(7)
f2=tree(8)
g2=tree(9)
h2=tree(10)
i2=tree(11)
x2.AddSuccessor(y2)
x2.AddSuccessor(z2)
x2.AddSuccessor(j2)
y2.AddSuccessor(d2)
y2.AddSuccessor(e2)
z2.AddSuccessor(c2)
d2.AddSuccessor(f2)
d2.AddSuccessor(g2)
d2.AddSuccessor(h2)
h2.AddSuccessor(i2)
x2.Print_DepthFirst()
print(x2.Get_LevelOrder())
binary1=x2.ConvertToBinaryTree()
binary1.Print_DepthFirst()
print(binary1.Get_LevelOrder())
general2=(binary1.ConvertToTree())[1]
if general2 != None:
	general2.Print_DepthFirst()
	print(general2.Get_LevelOrder())
else:
	print("cannot be converted")
