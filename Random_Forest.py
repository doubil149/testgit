import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
#from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


data=pd.read_csv('C:/Users/lenovo/Downloads/house-prices-advanced-regression-techniques/train.csv')

#nu=data.isnull().sum()

data=data.drop(['Alley','FireplaceQu','PoolQC','Fence','MiscFeature','Id'],axis=1)

x_obj=data.select_dtypes(include=["object"])

x_no_obj=data.select_dtypes(exclude=["object"])

la=preprocessing.LabelEncoder()
for i in range(x_obj.shape[1]):
    x_obj.iloc[:,i]=la.fit_transform(x_obj.iloc[:,i])
data=pd.concat([x_obj,x_no_obj],axis=1)

imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
clear_data=imputer.fit_transform(data)
new_data=pd.DataFrame(clear_data,columns=data.columns)

x=new_data.iloc[:,:-1]
y=new_data.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.70)
#model=LinearRegression()
#model=DecisionTreeRegressor(max_depth=50)
model=RandomForestRegressor()
model.fit(x_train,y_train)
print(model.score(x_train,y_train))
print(model.score(x_test,y_test))


plt.scatter(y_train,model.predict(x_train))
plt.show()
plt.scatter(y_test,model.predict(x_test),c='red')
plt.show()
