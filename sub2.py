import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


data=pd.read_csv('C:/Users/lenovo/Downloads/spaceship-titanic/train.csv')
test=pd.read_csv('C:/Users/lenovo/Downloads/spaceship-titanic/test.csv')
test_ids=test["PassengerId"]
 
#print(data.shape)
#print(test.shape)

nu=data.isnull().sum()
nu1=test.isnull().sum()
 
x=data.drop("Transported",axis=1)
y=data["Transported"]


x_obj=x.select_dtypes(include=["object"])
x_obj1=test.select_dtypes(include=["object"])

x_no_obj=x.select_dtypes(exclude=["object"])
x_no_obj1=test.select_dtypes(exclude=["object"])

la=preprocessing.LabelEncoder()
for i in range(x_obj.shape[1]):
    x_obj.iloc[:,i]=la.fit_transform(x_obj.iloc[:,i])
for i in range(x_obj1.shape[1]):
    x_obj1.iloc[:,i]=la.fit_transform(x_obj1.iloc[:,i])
    
x=pd.concat([x_obj,x_no_obj],axis=1)
test=pd.concat([x_obj1,x_no_obj1],axis=1)

imputer=SimpleImputer(missing_values=np.nan,strategy='mean')

clear_x=imputer.fit_transform(x)
clear_test=imputer.fit_transform(test)

new_x=pd.DataFrame(clear_x,columns=x.columns)
new_test=pd.DataFrame(clear_test,columns=test.columns)


x_train,x_test,y_train,y_test=train_test_split(new_x,y,train_size=0.60)
model=DecisionTreeClassifier().fit(x_train,y_train)

print(model.score(x_train,y_train))
submission_preds=model.predict(new_test)

df=pd.DataFrame({"PassengerId":test_ids.values, "Transported":submission_preds})
df.to_csv("submission2.csv",index=False)