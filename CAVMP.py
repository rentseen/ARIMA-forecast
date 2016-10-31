from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from matplotlib.pylab import rcParams
from statsmodels.tsa.arima_model import ARIMA
import random
import math
from operator import attrgetter
import time

start=time.time()


VM_RANGE=15
PM_NUMBER=20
NVM_NUMBER=600
U_MEAN=0.06111
SLICE_NUMBER=20
RAND_RANGE=0.6
P=3
Q=1
f=open("CAVMP_result2.txt","w")

def arimaPredict(originData):
	p=P
	q=Q
	#log
	logData=np.log(originData)
	predictData=[-1]
	#arima fit
	flag=False
	for i in range(p,-1,-1):
		if(flag):
			break
		for j in range(q,-1,-1):
			try:
				model = ARIMA(logData, order=(i, 0, j))
				resultsARIMA = model.fit(disp=-1)
				#predict
				predictData=resultsARIMA.predict(len(originData), len(originData), dynamic=True)
				#print(predictData)
				predictData=np.exp(predictData)
				if(math.isnan(predictData[0])):
					#print("----------------------")
					continue
				flag=True
				break
			except:
				continue
	
	if(predictData[0]==-1):
		print('bingo')
	#print(predictData[0])
	return predictData[0]+0.008

def generateU():
	#random
	x=[]
	base=random.randrange(0,6)
	for t in range(SLICE_NUMBER):
		tmp=(math.sin(base+t)+1+RAND_RANGE*random.random())*U_MEAN
		x.append(tmp)
	return x


class VM:

	def __init__(self):
		self.u=generateU()
		self.length=len(self.u)

	def predict(self):
		return arimaPredict(self.u)

	def addOneU(self,x):
		self.u.append(x)
		self.length=self.length+1

	def printU(self):
		print(self.u)

class PM:

	def __init__(self,x):
		self.length=random.randrange(VM_RANGE-5,VM_RANGE)
		self.vm=[]
		self.father=x
		self.load=-1
		self.num=-1
		for i in range(self.length):
			v=VM()
			self.vm.append(v)
	def __lt__(self, other):
		return self.load < other.load
	def compLoad(self):
		self.load=self.predict()
		#self.load=random.random()
	
	def predict(self):
		result=0
		for i in range(self.length):
			result=result+self.vm[i].predict()
		if(result>1):
			result=1
		return result

	def printU(self):
		for i in range(self.length):
			self.vm[i].printU()

class Rack:

	def __init__(self,x):
		self.length=PM_NUMBER
		self.pm=[]
		self.order=x
		for i in range(self.length):
			p=PM(self.order)
			self.pm.append(p)
	def printU(self):
		for i in range(self.length):
			self.pm[i].printU()
			print()

class NVM:
	def __init__(self):
		self.u=0.07+0.06*random.random()
		self.d=[]
		self.p=-1
		self.length=0
	def __lt__(self, other):
         return self.u < other.u
	def addD(self,x):
		self.d.append(x)
		self.length=self.length+1
	def printD(self):
		print(self.d)

#test p,q
'''
d=generateU()
x=arimaPredict(d)
d.append(x)
print(x)
plt.plot(d,color='red')
plt.show()
'''

'''
p=PM()
print(p.predict())
'''

for i in range(15):
	#Init rack

	rack=[]
	for i in range(64):
		tmp=Rack(i)
		rack.append(tmp)
	#rack[0].printU()

	#Init C
	C=[]
	for i in range(64):
		c=[]
		for j in range(64):
			c.append(0)
		C.append(c)

	flag=[]
	for i in range(64):
		flag.append(False)

	for i in range(64):
		if(flag[i]==False):
			flag[i]=True
			while(True):
				tmp=random.randrange(0,64)
				if(flag[tmp]==False):
					flag[tmp]=True
					C[i][tmp]=1
					C[tmp][i]=1
					break

	#Init epsilon
	epsilon=8



	#Init nvm
	nvm=[]
	for i in range(NVM_NUMBER):
		tmp=NVM()
		nvm.append(tmp)
	#Sort by u
	nvm.sort(reverse=True)
	'''
	for i in range(NVM_NUMBER):
		print(nvm[i].u)
	'''

	#Group
	flag=[]
	for i in range(NVM_NUMBER):
		flag.append(False)

	l=0
	while(l<NVM_NUMBER):
		gn=random.randrange(min(3,NVM_NUMBER-l),min(14,NVM_NUMBER-l)+1)
		g=[]
		for i in range(gn):
			x=random.randrange(0,NVM_NUMBER-l)
			x=x+1
			count=0
			pos=0
			while(count<x):
				while(flag[pos]):
					pos=pos+1
				count=count+1
				pos=pos+1
			g.append(pos-1)
			flag[pos-1]=True
			l=l+1

		for i in range(gn):
			for j in range(gn):
				if(i==j):
					continue
				nvm[g[i]].addD(g[j])


	pmList=[]
	for i in range(64):
		if(i%10==0):
			print('i= ',i)
		for j in range(rack[i].length):
			pmList.append(rack[i].pm[j])
			rack[i].pm[j].compLoad()

	pmList.sort()
	pmLength=len(pmList)
	for i in range(pmLength):
		pmList[i].num=i

	'''
	for i in range(len(pmList)):
		print(pmList[i].load)
	'''

	def ifConnect(i,j):
		x=pmList[i].father
		y=pmList[j].father
		if(x==y):
			return True
		if(C[x][y]==1):
			return True
		return False

	def ifChangeC(n,p):
		flag=False
		pos=-1
		for i in range(nvm[n].length):
			if(nvm[nvm[n].d[i]].p!=-1):
				for k in range(pmLength):
					if(pmList[k].num==nvm[nvm[n].d[i]].p):
						pos=k
						break
				if(not ifConnect(pos,p)):
					flag=True
					break
		return flag

	countC=0
	c=0
	for i in range(NVM_NUMBER):
		c=0
		for j in range(pmLength):
			c=c+1
			if(pmList[j].load+nvm[i].u<1):
				if(not ifChangeC(i,j)):
					nvm[i].p=pmList[j].num
					pmList[j].load=pmList[j].load+nvm[i].u
					pmList.sort()
					c=c-1
					break
		if(c==pmLength):
			countC=countC+2
			print("connect state changed")
			for j in range(pmLength):
				if(pmList[j].load+nvm[i].u<1):
					pmList[j].load=pmList[j].load+nvm[i].u
					break
			#for j in range(pmLength):
				#if(pmList[j].load+nvm[i].u<1):
					#nvm[i].p=j
					#change C

	pmList.sort()
	low=pmList[0].load
	high=pmList[pmLength-1].load

	sumU=0
	for i in range(pmLength):
		sumU=sumU+pmList[i].load
	evg=float(sumU)/pmLength


	f.write(str(countC))
	f.write('\t')
	f.write(str(low))
	f.write('\t')
	f.write(str(evg))
	f.write("\t")
	f.write(str(high))
	f.write("\n")

	print(str(countC))
	print(str(low))
	print(str(evg))
	print(str(high))

	print('countC is ', countC)



#Test nvm
'''
for i in range(NVM_NUMBER):
	nvm[i].printD()
'''



#Test generateU()
'''
x=generateU()
print(x)
originData=pd.Series(x)
originData.index = pd.Index(sm.tsa.datetools.dates_from_range('2001','2020'))
plt.plot(originData)
plt.show()
'''
f.close()
end=time.time()
print("run time",end-start)