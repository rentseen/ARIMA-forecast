from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 8

originData=[10930,10318,10595,10972,7706,6756,9092,10551,9722,10913,11151,8186,6422,6337,11649,11652,10310,12043,7937,6476,9662,9570,9981,9331,9449,6773,6304,9355,10477,10148,10395,11261,8713,7299,10424,10795,11069,11602,11427,9095,7707,10767,12136,12812,12006,12528,10329,7818,11719,11683,12603,11495,13670,11337,10232,13261,13230,15535,16837,19598,14823,11622,19391,18177,19994,14723,15694,13248,9543,12872,13101,15053,12619,13749,10228,9725,14729,12518,14564,15085,14722,11999,9390,13481,14795,15845,15271,14686,11054,10395]

originData=pd.Series(originData)
originData.index = pd.Index(sm.tsa.datetools.dates_from_range('2001','2090'))


#diff
diffData= originData.diff(1)
print(diffData)
diffData.dropna(inplace=True)


#select p,q
#fig = plt.figure(figsize=(12,8))
#2 rows 1 column: subplot 1
#ax1=fig.add_subplot(211)
#acf diagram, 
#q - The lag value where the ACF chart crosses the upper confidence interval for the first time
#fig = sm.graphics.tsa.plot_acf(diffData,lags=40,ax=ax1)
#2 rows 1 column: subplot 2
#ax2 = fig.add_subplot(212)
#pacf
#p - The lag value where the PACF chart crosses the upper confidence interval for the first time
#fig = sm.graphics.tsa.plot_pacf(diffData,lags=40,ax=ax2)
#fig.show()


from statsmodels.tsa.arima_model import ARIMA

originData=np.array(originData,dtype=np.float)
diffData=np.array(diffData,dtype=np.float)
model = ARIMA(originData, order=(7, 1, 1))
results_ARIMA = model.fit(disp=-1)

#plt.plot(diffData)
#plt.plot(results_ARIMA.fittedvalues, color='red')
#plt.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-diffData)**2))
#plt.show()


result=np.insert(results_ARIMA.fittedvalues,0,10930)
for i in range(len(results_ARIMA.fittedvalues)):
	if(i==0):
		continue
	result[i]=originData[i-1]+result[i]

plt.plot(originData)
plt.plot(result, color='red')
plt.show()



#plt.show()