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

VM_RANGE=15
PM_NUMBER=20
U_MEAN=0.075
SLICE_NUMBER=20
RAND_RANGE=0.6

def arimaPredict(originData):
	#log
	logData=np.log(originData)
	#arima fit
	model = ARIMA(logData, order=(2, 1, 1))
	resultsARIMA = model.fit(disp=-1)
	#predict
	predictData=resultsARIMA.predict(len(originData), len(originData), dynamic=True)
	#print(predictData)
	return predictData[0]

def generateU():
	#random
	x=[]
	base=random.randrange(0,6)
	for t in range(SLICE_NUMBER):
		tmp=(math.sin(base+t)+1+RAND_RANGE*random.random())*0.0577
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

	def __init__(self):
		self.length=random.randrange(VM_RANGE-5,VM_RANGE)
		self.vm=[]
		for i in range(self.length):
			v=VM()
			self.vm.append(v)
	
	def predict(self):
		result=0
		for i in range(self.length):
			result=result+self.vm[i].predict()
		return result

	def printU(self):
		for i in range(self.length):
			self.vm[i].printU()

class Rack:

	def __init__(self):
		self.length=PM_NUMBER
		self.pm=[]
		for i in range(self.length):
			p=PM()
			self.pm.append(p)
	def printU(self):
		for i in range(self.length):
			self.pm[i].printU()
			print()



'''
for i in range(4):
	for j in range(3):
		print(generateU())
	print()
'''


'''
#Init rack
rack=[]
for i in range(64):
	tmp=Rack()
	rack.append(tmp)

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
'''
x=generateU()
print(x)
originData=pd.Series(x)
originData.index = pd.Index(sm.tsa.datetools.dates_from_range('2001','2020'))
plt.plot(originData)
plt.show()