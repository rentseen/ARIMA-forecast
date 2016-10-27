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
plt.plot(y)
plt.show()
print y