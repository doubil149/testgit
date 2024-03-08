import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


data=pd.read_csv('C:/Users/lenovo/Downloads/Iris.csv')

data=data.drop(['label'],axis=1)


c_num=[]
j=[]

model=KMeans(n_clusters=4)
model.fit(data)
   


