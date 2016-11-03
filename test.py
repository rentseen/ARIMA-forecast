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
'''
import re
import matplotlib.pyplot as plt
import math

f1=open("static-result.txt","r")
f2=open("CAVMP-result.txt","r")
f3=open("CAstatic-result.txt","r")

o1=open("u-static.txt","w")
o2=open("u-CAVMP.txt","w")
o3=open("u-CAstatic.txt","w")

x1=f1.read()
x1=re.split('\n|\t',x1)
x1.pop()

x2=f2.read()
x2=re.split('\n|\t',x2)
x2.pop()

x3=f3.read()
x3=re.split('\n|\t',x3)
x3.pop()

p1_l=[]
p1_h=[]
p1_a=[]
p2_l=[]
p2_h=[]
p2_a=[]
p3_l=[]
p3_h=[]
p3_a=[]

for i in range(0,len(x1),4):
	p1_l.append(float(x1[i+1]))
	p1_h.append(float(x1[i+2]))
	p1_a.append(float(x1[i+3]))

for i in range(0,len(x2),4):
	p2_l.append(float(x2[i+1]))
	p2_a.append(float(x2[i+2]))
	p2_h.append(float(x2[i+3]))

for i in range(0,len(x3),4):
	p3_l.append(float(x3[i+1]))
	p3_h.append(float(x3[i+2]))
	p3_a.append(float(x3[i+3]))

p1_l_a=sum(p1_l)/len(p1_l)
p2_l_a=sum(p2_l)/len(p2_l)
p3_l_a=sum(p3_l)/len(p3_l)

p1_a_a=sum(p1_a)/len(p1_a)
p2_a_a=sum(p2_a)/len(p2_a)
p3_a_a=sum(p3_a)/len(p3_a)

p1_h_a=sum(p1_h)/len(p1_h)
p2_h_a=sum(p2_h)/len(p2_h)
p3_h_a=sum(p3_h)/len(p3_h)

print p1_l_a
print p1_h_a
print p1_a_a
print p2_l_a
print p2_h_a
print p2_a_a
print p3_l_a
print p3_h_a
print p3_a_a

o1.write(str(p1_l_a))
o1.write("\t")
o1.write(str(p1_h_a))
o1.write("\t")
o1.write(str(p1_a_a))
o1.write("\n")

o2.write(str(p2_l_a))
o2.write("\t")
o2.write(str(p2_h_a))
o2.write("\t")
o2.write(str(p2_a_a))
o2.write("\n")

o3.write(str(p3_l_a))
o3.write("\t")
o3.write(str(p3_h_a))
o3.write("\t")
o3.write(str(p3_a_a))
o3.write("\n")
