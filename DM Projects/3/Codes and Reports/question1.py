"""
Created on Sun Dec 19 19:05:41 2021

@author: User
"""
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
#reading data
data1 = pd.read_csv('data1.csv')
data2 = pd.read_csv('data2.csv')
#seperating train and test (partition is 90 to 10)
#data1
data1_train,data1_test = train_test_split(data1,train_size = 0.8,test_size=0.2)
#data2
data2_train,data2_test = train_test_split(data2,train_size = 0.8,test_size=0.2)
#creating our linear classifier
#data1
linear_classifier1 = LinearSVC()
linear_classifier1.fit(data1_train[['X','Y']],data1_train['Class'])
#data2
linear_classifier2 = LinearSVC()
linear_classifier2.fit(data2_train[['X','Y']],data2_train['Class'])
#function below is for checking accuracy of linear and non linear svm
def accuracy(testData,classifier):
    acc = 0
    for i in range(len(testData)):
        predicted_lable = classifier.predict([testData[['X','Y']].iloc[i]])[0]
        if predicted_lable == testData['Class'].iloc[i]:
            acc += 1
    return acc / len(testData)
#seeing the accuracy of linear data
print('data1 linear accuracy: ',accuracy(data1_test, linear_classifier1))
print('data2 linear accuracy: ',accuracy(data2_test, linear_classifier2))
#non linear svc for data2
nonlinear_classifier2 = svm.NuSVC()
nonlinear_classifier2.fit(data2_train[['X','Y']],data2_train['Class'])
print('data2 non linear accuracy:',accuracy(data2_test,nonlinear_classifier2))
#plotting hyper plane
#plotting for data1 linear form
print('data1 linear')
plt.scatter(data1['X'][(data1['Class'] == 1)],data1['Y'][(data1['Class'] == 1)],color = 'red')
plt.scatter(data1['X'][(data1['Class'] == 0)],data1['Y'][(data1['Class'] == 0)],color = 'green')
plt.show()
#plotting for data2 linear form
print('data2 linear')
plt.scatter(data2['X'][(data2['Class'] == 1)],data2['Y'][(data2['Class'] == 1)],color = 'red')
plt.scatter(data2['X'][(data2['Class'] == 0)],data2['Y'][(data2['Class'] == 0)],color = 'green')
plt.show()
#plotting for data2 non linear form
print('data2 non linear')
plt.scatter(data2['X'][(data2['Class'] == 1)],data2['Y'][(data2['Class'] == 1)],color = 'red')
plt.scatter(data2['X'][(data2['Class'] == 0)],data2['Y'][(data2['Class'] == 0)],color = 'green')
plt.show()

            

