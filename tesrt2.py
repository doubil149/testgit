import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data=pd.read_csv('StudentsPerformance.csv')

x=data.iloc[:,:-1]
y=data.iloc[:,-1]

print(data.isnull().sum())

x_obj=x.select_dtypes(include=["object"])
x_no_obj=x.select_dtypes(exclude=["object"])

la=LabelEncoder()
for i in range(x_obj.shape[1]):
    x_obj.iloc[:,i]=la.fit_transform(x_obj.iloc[:,i])
X=pd.concat([x_obj,x_no_obj],axis=1)
print(X)

x_train,x_test,y_train,y_test=train_test_split(X,y,train_size=0.6)
m=LinearRegression()
m.fit(x_train,y_train)

print(m.score(x_train,y_train))
print(m.score(x_test,y_test))
print(x_train.shape)
print(type(y_train))

plt.scatter(x_train,y_train)
plt.plot(x_train,m.predict(x_train))
#plt.scatter(x_test,y_test)
#plt.plot(x_test,m.predict(x_test))
plt.show