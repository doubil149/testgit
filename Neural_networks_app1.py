import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

data=pd.read_csv('C:/Users/lenovo/Downloads/Iris.csv')
#print('data')

x=data.iloc[:,:-1]
y=data.iloc[:,-1]


x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.95,random_state=0)

model=MLPRegressor()
model.fit(x_train,y_train)

print(model.score(x_train,y_train))
print(model.score(x_test,y_test))

plt.scatter(y_train,model.predict(x_train),marker='o',c='red',s=50)
plt.scatter(y_test,model.predict(x_test))
