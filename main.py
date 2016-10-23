from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from statsmodels.tsa.arima_model import ARIMA
from matplotlib.pylab import rcParams
import random
import math
#ACF and PACF plots:
from statsmodels.tsa.stattools import acf, pacf

RAND_RANGE=0.6
SLICE_NUMBER=20

def generateU():
	#random
	x=[]
	base=random.randrange(0,6)
	for t in range(SLICE_NUMBER):
		tmp=(math.sin(base+t)+1+RAND_RANGE*random.random())*0.0577
		x.append(tmp)
	return x

rcParams['figure.figsize'] = 15, 8

originData=generateU()
#origin data
originData=pd.Series(originData)
originData.index = pd.Index(sm.tsa.datetools.dates_from_range('2001','2020'))

#log data, filter the extremum
logData=np.log(originData)

#diff data
diffData= logData
diffData.dropna(inplace=True)

print(diffData)

'''
lag_acf = acf(diffData, nlags=SLICE_NUMBER-2)
lag_pacf = pacf(diffData, nlags=SLICE_NUMBER-2, method='ols')

#Plot ACF: 
#q - The lag value where the ACF chart crosses the upper confidence interval for the first time
plt.subplot(211) 
plt.plot(lag_acf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(diffData)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(diffData)),linestyle='--',color='gray')
plt.title('Autocorrelation Function')

#Plot PACF:
#p - The lag value where the PACF chart crosses the upper confidence interval for the first time
plt.subplot(212)
plt.plot(lag_pacf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(diffData)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(diffData)),linestyle='--',color='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()
plt.show()
'''

#select p,q
'''
fig = plt.figure(figsize=(12,8))
#2 rows 1 column: subplot 1
ax1=fig.add_subplot(211)
#acf diagram, 
#q - The lag value where the ACF chart crosses the upper confidence interval for the first time
fig = sm.graphics.tsa.plot_acf(diffData,lags=15,ax=ax1)
#2 rows 1 column: subplot 2
ax2 = fig.add_subplot(212)
#pacf
#p - The lag value where the PACF chart crosses the upper confidence interval for the first time
fig = sm.graphics.tsa.plot_pacf(diffData,lags=15,ax=ax2)
fig.show()
tmp=input()
'''


#fit

model = ARIMA(logData, order=(3, 0, 1))
results_ARIMA = model.fit(disp=-1)
test=results_ARIMA.predict('2021', '2021', dynamic=True)

result=logData.head(1)
result=result.append(results_ARIMA.fittedvalues)
plt.plot(logData)
plt.plot(result, color='red')
plt.plot(test, color='black')
plt.show()

#print(results_ARIMA.aic,results_ARIMA.bic,results_ARIMA.hqic)


#show fit value
'''
plt.plot(diffData)
#plt.plot(results_ARIMA.fittedvalues, color='red')
plt.plot(test, color='black')
plt.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-diffData)**2))
plt.show()
'''
'''
result=logData.head(1)

result=result.append(results_ARIMA.fittedvalues)

for i in range(len(result)):
	if(i==0):
		continue
	result[i]=logData[i-1]+result[i]

plt.plot(originData)
predictData=np.exp(result)
plt.plot(predictData, color='red')
plt.show()
'''




#plt.show()