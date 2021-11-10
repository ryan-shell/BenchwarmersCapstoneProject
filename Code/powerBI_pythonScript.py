import pickle
import pandas as pd
import numpy as np

filename = r'C:\Dev10Projects\_classPhase\pythonPractice\pandas\ML_Cstone_pt2\gradientboostmodel_grouped'
gmodel = pickle.load(open(filename,'rb'))
dataset.drop(columns=['JP_Sales','NA_Sales','Other_Sales','PAL_Sales','timestamp','Rank'])
dataset.dropna(inplace=True)
oneDev = dataset.groupby('Developer').filter(lambda x:len(x) == 1)
twoDev = dataset.groupby('Developer').filter(lambda x:len(x) == 2)
threeDev = dataset.groupby('Developer').filter(lambda x:len(x) == 3)
fourDev = dataset.groupby('Developer').filter(lambda x:len(x) == 4)
popDev = dataset.groupby('Developer').filter(lambda x:len(x) >= 5)
oneDev['Developer'] = 'OneHits'
twoDev['Developer'] = 'TwoHits'
threeDev['Developer'] = 'ThreeHits'
fourDev['Developer'] = 'FourHits'
concatDevs = pd.concat([oneDev,twoDev,threeDev,fourDev,popDev])

onePub = concatDevs.groupby('Publisher').filter(lambda x:len(x) == 1)
twoPub = concatDevs.groupby('Publisher').filter(lambda x:len(x) == 2)
threePub = concatDevs.groupby('Publisher').filter(lambda x:len(x) == 3)
fourPub = concatDevs.groupby('Publisher').filter(lambda x:len(x) == 4)
popPub = concatDevs.groupby('Publisher').filter(lambda x:len(x) >= 5)

onePub['Publisher'] = 'OnePubs'
twoPub['Publisher'] = 'TwoPubs'
threePub['Publisher'] = 'ThreePubs'
fourPub['Publisher'] = 'FourPubs'

concatVg = pd.concat([onePub,twoPub,threePub,fourPub,popPub])
concatVg['NameLength'] = concatVg['Name'].str.len()
concatVg['log_Global_Sales'] = (np.log(concatVg['Global_Sales']))
originalsales = concatVg['log_Global_Sales']

newvg = concatVg[['NameLength','Critic_Score','ESRB_Rating','Genre','Platform','Publisher','Developer','Year']]
vgc2 = pd.get_dummies(newvg, columns=['ESRB_Rating','Genre','Platform','Developer','Publisher'], drop_first=True)

ypred = gmodel.predict(vgc2)
vgc2['Predicted_GlobalSales'] = np.exp(ypred)
vgc2['Actual_GlobalSales'] = np.exp(originalsales)
vgc2['log_predictedSales'] = ypred
vgc2['log_actualSales'] = originalsales
