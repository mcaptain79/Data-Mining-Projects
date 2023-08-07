"""
Created on Thu Dec 16 20:08:17 2021

@author: User
"""
import pandas as pd
import random
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import math
#reading data
data = pd.read_csv('data4.csv')
#preprocessing our data
#elimination of instances with missing value
data = data.dropna()
data = data.reset_index()
#covertion of pclass column
for i in range(len(data)):
    if data['Pclass'][i] == 1:
        data['Pclass'][i] = 'one'
    elif data['Pclass'][i] == 2:
        data['Pclass'][i] = 'two'
    else:
        data['Pclass'][i] = 'three'
#convertion of target class
for i in range(len(data)):
    if data['Target_class'][i] == 1:
        data['Target_class'][i] = 'one'
    else:
        data['Target_class'][i] = 'zero'
#covertion of Age class
for i in range(len(data)):
    if data['Age'][i] < 10:
        data['Age'][i] = 'A'
    elif 10 <= data['Age'][i] < 20:
        data['Age'][i] = 'B'
    elif 20 <= data['Age'][i] < 30:
        data['Age'][i] = 'C'
    elif 30 <= data['Age'][i] < 40:
        data['Age'][i] = 'D'
    elif 40 <= data['Age'][i] < 50:
        data['Age'][i] = 'E'
    else:
        data['Age'][i] = 'F'
lb = LabelEncoder()
for i in data:
    data[i] = lb.fit_transform(data[i])
#saving our data in array
dataArray = []
for i in range(len(data)):
    dataArray.append(data.loc[i])
#initializing weights
weightsList = [1/len(data)]*len(data)
#list below is for correct predic staus
statusList = [False]*len(data)
#algorithm below is for implementation of ada boost
#using naive bayes as classifier
gnb = GaussianNB()
#number of boosting rounds
k = 10
#numbers of samples boost
samples_number = math.floor(len(data)*0.8)
for i in range(k):
    dataSamples = random.choices(dataArray,weights = weightsList,k = samples_number)
    dataFrameSamples = pd.DataFrame(dataSamples)
    #learning based on selected samples
    gnb.fit(dataFrameSamples[['Pclass','Sex','Age']],dataFrameSamples['Target_class'])
    error = 0
    for i in range(len(data)):
        predictedLable = gnb.predict([data[['Pclass','Sex','Age']].iloc[i]])[0]
        if predictedLable == data['Target_class'][i]:
            statusList[i] = True
        else:
            statusList[i] = False
            error += weightsList[i]
    error /= len(data)
    print('err:',error)
    alfa = math.log((1-error)/error,math.e)/2
    for i in range(len(data)):
        if statusList[i] == True:
            weightsList[i] *= math.e**(-1*alfa)
        else:
            weightsList[i] *= math.e**(alfa)
    for i in range(len(weightsList)):
        weightsList[i] /= sum(weightsList) 
    #creating confusion matrix
    tp = 1
    fn = 1
    fp = 1
    tn = 1
    for i in range(len(data)):
        predictedLable = gnb.predict([data[['Pclass','Sex','Age']].iloc[i]])[0]
        if predictedLable == 1 and data['Target_class'][i] == 1:
            tp += 1
        elif predictedLable == 1 and data['Target_class'][i] == 0:
            fn += 1
        elif predictedLable == 0 and data['Target_class'][i] == 1:
            fp += 1
        else:
            tn += 1
    print('true positive:',tp-1)
    print('false negative:',fn-1)
    print('false positive:',fp-1)
    print('true negative:',tn-1)
    print('precision:',(tp)/(fp+tp))
    print('recall:',(tp)/(fn+tp))
    print('--------------------------------')