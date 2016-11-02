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
'''
import matplotlib.pyplot as plt
f=open("C-static.txt","r")
out=open("C-CDF-static.txt","w")
x=f.read()
x=x.split('\n')
y=x[:100]
for i in range(100):
	y[i]=int(y[i])
y.sort()
'''
'''p=open("sort.txt","w")
for i in range(100):
	y[i]=str(y[i])
for i in range(100):
	p.write(y[i])
	p.write("\n")
'''
'''
m=[]
n=[]
m.append(y[0])
n.append(0.01)
length=0
for i in range(1,100):
	if(m[length]==y[i]):
		n[length]=n[length]+0.01
	else:
		m.append(y[i])
		n.append(n[length]+0.01)
		length=length+1
print m
print n
for i in range(len(m)):
	out.write(str(m[i]))
	out.write("\t")
	out.write(str(n[i]))
	out.write("\n")
out.close()
plt.plot(m,n)
plt.show()
'''
f1=open("C-CDF-static.txt","r")
f2=open("C-CDF-CAVMP.txt","r")
f3=open("C-CDF-CAstatic.txt","r")

x1=f1.read()
x1=x1.split('\n')
y1=x1[:100]
