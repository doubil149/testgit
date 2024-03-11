import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data=pd.read_csv('C:/Users/lenovo/Downloads/titanic/train.csv')
test=pd.read_csv('C:/Users/lenovo/Downloads/titanic/test.csv')
test_ids=test["PassengerId"]
 
#print(data.shape)
#print(test.shape)

nu=data.isnull().sum()
nu1=test.isnull().sum()

data=data.drop(['Cabin','Name','Ticket','PassengerId'],axis=1)
test=test.drop(['Cabin','Name','Ticket','PassengerId'],axis=1)

x_obj=data.select_dtypes(include=["object"])
x_obj1=test.select_dtypes(include=["object"])

x_no_obj=data.select_dtypes(exclude=["object"])
x_no_obj1=test.select_dtypes(exclude=["object"])

la=preprocessing.LabelEncoder()
for i in range(x_obj.shape[1]):
    x_obj.iloc[:,i]=la.fit_transform(x_obj.iloc[:,i])
for i in range(x_obj1.shape[1]):
    x_obj1.iloc[:,i]=la.fit_transform(x_obj1.iloc[:,i])
    
data=pd.concat([x_obj,x_no_obj],axis=1)
test=pd.concat([x_obj1,x_no_obj1],axis=1)

imputer=SimpleImputer(missing_values=np.nan,strategy='mean')

clear_data=imputer.fit_transform(data)
clear_test=imputer.fit_transform(test)

new_data=pd.DataFrame(clear_data,columns=data.columns)
new_test=pd.DataFrame(clear_test,columns=test.columns)

x=new_data.drop("Survived",axis=1)
y=new_data["Survived"]

x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.60)
model=LogisticRegression().fit(x_train,y_train)

print(model.score(x_train,y_train))
submission_preds=model.predict(new_test)

df=pd.DataFrame({"PassengerId":test_ids.values, "Survived":submission_preds})
df.to_csv("submission.csv",index=False)