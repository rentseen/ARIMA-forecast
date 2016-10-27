'''
class T:
	def __init__(self):
		self.x=10
		self.y=20

a=T()
b=[]
b.append(a)

print(a.x)
print(b[0].x)

a.x=-1

print(a.x)
print(b[0].x)
'''
import matplotlib.pyplot as plt
f=open("result.txt","r")
x=f.read()
x=x.split('\n')
y=x[:100]
for i in range(100):
	y[i]=int(y[i])
y.sort()
'''p=open("sort.txt","w")
for i in range(100):
	y[i]=str(y[i])
for i in range(100):
	p.write(y[i])
	p.write("\n")
'''
m=[]
n=[]
m.append(y[0])
n.append(1)
length=0
for i in range(1,100):
	if(m[length]==y[i]):
		n[length]=n[length]+1
	else:
		m.append(y[i])
		n.append(1)
		length=length+1
print m
print n
plt.plot(m,n)
plt.show()