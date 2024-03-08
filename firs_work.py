import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing


data=pd.read_csv('StudentsPerformance.csv')
data=data.drop(['race/ethnicity','test preparation course'],axis=1)
object_data=data.select_dtypes(include=['object'])
print(object_data)
le=preprocessing.LabelEncoder()
for i in range(object_data.shape[1]):
    object_data.iloc[:,i]=le.fit_transform(object_data.iloc[:,i])
print(object_data) 
num_data= data.select_dtypes(exclude=['object']) 
data=pd.concat([object_data,num_data],axis=1)
print(data)
c=data.corr()
print(c)
sns.heatmap(c,annot=True) 
plt.show()