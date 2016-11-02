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
import re
import matplotlib.pyplot as plt
import math
f1=open("C-CDF-static.txt","r")
f2=open("C-CDF-CAVMP.txt","r")
f3=open("C-CDF-CAstatic.txt","r")

o1=open("CDF-static.txt","w")
o2=open("CDF-CAVMP.txt","w")
o3=open("CDF-CAstatic.txt","w")

x1=f1.read()
x1=re.split('\n|\t',x1)
x1.pop()

x2=f2.read()
x2=re.split('\n|\t',x2)
x2.pop()

x3=f3.read()
x3=re.split('\n|\t',x3)
x3.pop()


p1_x=[]
p1_y=[]
p2_x=[]
p2_y=[]
p3_x=[]
p3_y=[]

for i in range(0,len(x1),2):
	p1_x.append(float(x1[i])/500)
	p1_y.append(float(x1[i+1]))

for i in range(0,len(x2),2):
	p2_x.append(float(x2[i])/500)
	p2_y.append(float(x2[i+1]))

for i in range(0,len(x3),2):
	p3_x.append(float(x3[i])/500)
	p3_y.append(float(x3[i+1]))

for i in range(len(p1_x)):
	o1.write(str(p1_x[i]))
	o1.write('\t')
	o1.write(str(p1_y[i]))
	o1.write('\n')

for i in range(len(p2_x)):
	o2.write(str(p2_x[i]))
	o2.write('\t')
	o2.write(str(p2_y[i]))
	o2.write('\n')
for i in range(len(p3_x)):
	o3.write(str(p3_x[i]))
	o3.write('\t')
	o3.write(str(p3_y[i]))
	o3.write('\n')

plt.plot(p1_x,p1_y,p2_x,p2_y,p3_x,p3_y)
plt.ylim(0,1.1)
plt.show()
