"""
Created on Mon Dec 20 20:15:46 2021

@author: mcaptain79
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
data = pd.read_csv('data3.csv')
features = ['sepal_length','sepal_width','petal_length','petal_width']
#preprocessing data
lb = LabelEncoder()
for i in data:
    data[i] = lb.fit_transform(data[i])
#splitting train and test data
dataTrain,dataTest = train_test_split(data,train_size = 0.8,test_size = 0.2)
#creating our random forest classifiers
#with 10 trees
randomForest1 = RandomForestClassifier(n_estimators = 10)
randomForest1.fit(dataTrain[features],dataTrain['species'])
#with 30 tress
randomForest2 = RandomForestClassifier(n_estimators = 30)
randomForest2.fit(dataTrain[features],dataTrain['species'])
#with 50 trees
randomForest3 = RandomForestClassifier(n_estimators = 50)
randomForest3.fit(dataTrain[features],dataTrain['species'])
#with 70 trees
randomForest4 = RandomForestClassifier(n_estimators = 70)
randomForest4.fit(dataTrain[features],dataTrain['species'])
#with 90 trees
randomForest5 = RandomForestClassifier(n_estimators = 90)
randomForest5.fit(dataTrain[features],dataTrain['species'])
#with 120 trees
randomForest6 = RandomForestClassifier(n_estimators = 120)
randomForest6.fit(dataTrain[features],dataTrain['species'])
#function below if for calculation accuracy
def accuracy(test,model):
    acc = 0
    for i in range(len(test)):
        predictedLable = model.predict(test[features])[0]
        if predictedLable == test['species'].iloc[i]:
            acc += 1
    return acc/len(test)
print('10 trees accuracy:',accuracy(dataTest, randomForest1))
print('30 trees accuracy:',accuracy(dataTest, randomForest2))
print('50 trees accuracy:',accuracy(dataTest, randomForest3))
print('70 trees accuracy:',accuracy(dataTest, randomForest4))
print('90 trees accuracy:',accuracy(dataTest, randomForest5))
print('120 trees accuracy:',accuracy(dataTest, randomForest6))
        



