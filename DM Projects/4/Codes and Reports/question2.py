"""
Created on Mon Jan  3 16:10:03 2022

@author: mcaptain79
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC,SVC
#reading data drom exel
myData = pd.read_excel('dataset2.xlsx')
#function below is for implemetation pca
def pca(data,r):
    m = np.mean(data)#compute mean
    z = data - np.transpose(m)#centre data
    sigma = (1/len(data))*(np.transpose(z) @ z)#compute covariance matrix
    y,U = np.linalg.eig(sigma)#compute eigen values and eigen vectors
    Ur = U[:,:r]#reduced basis
    A = np.zeros((r,len(data)))#reduced dimentionality
    for i in range(len(data)):
        A[:,i] = np.transpose(Ur) @ np.transpose(data.iloc[i,:]) 
    return np.transpose(A)
#applying algorithm with data reduced to 2 dimentions
dataReduced = pca(myData[['A','B','C','D']], 2)
realClass = myData['class']
#creating matrix with two features and class lable
newDataMatrix = np.zeros((150,3))
newDataMatrix[:,0:2] = dataReduced
newDataMatrix[:,2] = realClass
#craeting data frame of that matrix and splitting test and train
newDataFrame = pd.DataFrame(newDataMatrix)
trainData,testData = train_test_split(newDataFrame,test_size = 0.2,train_size = 0.8)
#function below is for calculating accuracy
def accuracy_calculate(data,lables,model):
    accuracy = 0
    for i in range(len(data)):
        predictedLable = model.predict([data.iloc[i]])
        if predictedLable == lables.iloc[i]:
            accuracy += 1
    return accuracy / len(data)
#creating linear and non linear svm
linearSvm = LinearSVC()
nonLinearSvm = SVC()
linearSvm.fit(trainData[[0,1]],trainData[2])
nonLinearSvm.fit(trainData[[0,1]],trainData[2])
#checking accuracy
print('linear svm accuracy:',accuracy_calculate(testData[[0,1]], testData[2], linearSvm))
print('non linear svm accuracy:',accuracy_calculate(testData[[0,1]], testData[2], nonLinearSvm))

        
    
