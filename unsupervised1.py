import pandas as pd
from sklearn.cluster import KMeans
import matplotlib as plt



data=pd.read_csv('C:/Users/lenovo/Downloads/Iris.csv')

data=data.drop(['label'],axis=1)


c_num=[]
j=[]
 
for i in range(1,10):
    model=KMeans(n_clusters=i)
    model.fit(data)
    c_num.append(i)
    j.append(model.inertia_)
plt.scatter(c_num,j)
plt.show()