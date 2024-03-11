import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


data=pd.read_csv('C:/Users/lenovo/Downloads/playground-series-s4e3/train.csv')
test=pd.read_csv('C:/Users/lenovo/Downloads/playground-series-s4e3/test.csv')
test_ids=test["id"]
 
#print(data.shape)
#print(test.shape)

nu=data.isnull().sum()
nu1=test.isnull().sum()
 
x=data.drop(["Pastry","Z_Scratch","K_Scatch","Stains","Dirtiness","Bumps","Other_Faults"],axis=1)
y=data["Pastry"]
y1=data["Z_Scratch"]
y2=data["K_Scatch"]
y3=data["Stains"]
y4=data["Dirtiness"]
y5=data["Bumps"]
y6=data["Other_Faults"]

#x_obj=x.select_dtypes(include=["object"])
#x_obj1=test.select_dtypes(include=["object"])

#x_no_obj=x.select_dtypes(exclude=["object"])
#x_no_obj1=test.select_dtypes(exclude=["object"])

#la=preprocessing.LabelEncoder()
#for i in range(x_obj.shape[1]):
    #x_obj.iloc[:,i]=la.fit_transform(x_obj.iloc[:,i])
#for i in range(x_obj1.shape[1]):
 #   x_obj1.iloc[:,i]=la.fit_transform(x_obj1.iloc[:,i])
    
#x=pd.concat([x_obj,x_no_obj],axis=1)
#test=pd.concat([x_obj1,x_no_obj1],axis=1)

#imputer=SimpleImputer(missing_values=np.nan,strategy='mean')

#clear_x=imputer.fit_transform(x)
#clear_test=imputer.fit_transform(test)

#new_x=pd.DataFrame(clear_x,columns=x.columns)
#new_test=pd.DataFrame(clear_test,columns=test.columns)


x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.70)
model=DecisionTreeRegressor().fit(x_train,y_train)

print(model.score(x_train,y_train))
submission_preds=model.predict(test)

df=pd.DataFrame({"id":test_ids.values,["Pastry","Z_Scratch","K_Scatch","Stains","Dirtiness","Bumps","Other_Faults"] :submission_preds})
df.to_csv("submission3.csv",index=False)