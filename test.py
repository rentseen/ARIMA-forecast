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
'''
import re
import matplotlib.pyplot as plt
import math

f1=open("static_result_4_4.txt","r")
f2=open("CAVMP_result_4_4.txt","r")
f3=open("CAstatic_result_4_4.txt","r")

o1=open("u-static-4-4.txt","w")
o2=open("u-CAVMP-4-4.txt","w")
o3=open("u-CAstatic-4-4.txt","w")

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
'''

import numpy as np
import matplotlib.pyplot as plt

N=3

aveCAVMPMeans=[0.946601801623,0.947113559077,0.948454096069]
lowCAVMPMeans=[0.810084820106,0.767802605805,0.76494951005]
highCAVMPMeans=[1.0,1.0,1.0]

stdCAVMP=[]
tmp1=[]
tmp2=[]
for i in range(3):
	tmp1.append(aveCAVMPMeans[i]-lowCAVMPMeans[i])
	tmp2.append(highCAVMPMeans[i]-aveCAVMPMeans[i])
stdCAVMP.append(tmp1)
stdCAVMP.append(tmp2)

aveCAstaticMeans=[0.955477854026,0.953211106968,0.953266175663]
lowCAstaticMeans=[0.616405792127,0.515454403091,0.435178540951]
highCAstaticMeans=[1.0,1.0,1.0]

stdCAstatic=[]
tmp1=[]
tmp2=[]
for i in range(3):
	tmp1.append(aveCAstaticMeans[i]-lowCAstaticMeans[i])
	tmp2.append(highCAstaticMeans[i]-aveCAstaticMeans[i])
stdCAstatic.append(tmp1)
stdCAstatic.append(tmp2)

avestaticMeans=[0.953938547729,0.952260320505,0.95265016232]
lowstaticMeans=[0.615834126982,0.515247980872,0.436673392773]
highstaticMeans=[1.0,1.0,1.0]

stdStatic=[]
tmp1=[]
tmp2=[]
for i in range(3):
	tmp1.append(avestaticMeans[i]-lowstaticMeans[i])
	tmp2.append(highstaticMeans[i]-avestaticMeans[i])
stdStatic.append(tmp1)
stdStatic.append(tmp2)

ind = np.arange(N)
width = 0.2

p1 = plt.bar(ind+0.2, aveCAVMPMeans, width, color='r', yerr=stdCAVMP)
p2 = plt.bar(ind+0.4, aveCAstaticMeans, width, color='b', yerr=stdCAstatic)
p3 = plt.bar(ind+0.6, avestaticMeans, width, color='g', yerr=stdStatic)


plt.ylabel('Utilization')
plt.xlabel('Scale of Cloud /racks')
plt.title('Load balance')
plt.xticks(ind + width/2+0.4, ('2x2', '4x4', '8x8'))
plt.yticks((0,0.2,0.4,0.6,0.8,1.0,1.2,1.4))
plt.legend((p1[0], p2[0], p3[0]), ('CAVMP', 'CAstatic','static'))

plt.show()
