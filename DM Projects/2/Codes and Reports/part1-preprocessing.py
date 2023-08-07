"""
Created on Tue Nov 23 18:42:46 2021

@author: mcaptain79
"""
import pandas as pd
import pickle
#function below is for coverting age numbers to names
def age_modification(data):
    for i in range(len(data)):
        if data['age'][i] < 10:
            data['age'][i] = 'kid'
        elif 10 <= data['age'][i] < 20:
            data['age'][i] = 'teenage'
        elif 20 <= data['age'][i] < 30:
            data['age'][i] = 'teen'
        elif 30 <= data['age'][i] < 40:
            data['age'][i] = 'mature'
        elif 40 <= data['age'][i] < 50:
            data['age'][i] = 'middle aged'
        elif 50 <= data['age'][i] < 70:
            data['age'][i] = 'old'
        else:
            data['age'][i] = 'phosil'
#function below is for coverting income numbers to names
def income_modification(data):
    for i in range(len(data)):
        if data['income'][i] == '<=50K':
            data['income'][i] = 'low'
        else:
            data['income'][i] = 'high'
#function below is for coverting hours per week numbers to names
def hour_modification(data):
    for i in range(len(data)):
        if int(data['hours-per-week'][i]) < 10:
           data['hours-per-week'][i] = 'lazy'
        elif 10 <= int(data['hours-per-week'][i]) < 30:
            data['hours-per-week'][i] = 'semi lazy'
        elif 30 <= int(data['hours-per-week'][i]) < 50:
            data['hours-per-week'][i] = 'middle working'
        elif 50 <= int(data['hours-per-week'][i]) < 70:
            data['hours-per-week'][i] = 'working'
        else:
            data['hours-per-week'][i] = 'hard working'
#function below is for coverting capital-loss numbers to names
def capital_loss_modification(data):
    for i in range(len(data)):
        if int(data['capital-loss'][i]) < 1000:
            data['capital-loss'][i] = 'very low'
        elif 1000 <= int(data['capital-loss'][i]) < 2000:
            data['capital-loss'][i] = 'low'
        elif 2000 <= int(data['capital-loss'][i]) < 3000:
            data['capital-loss'][i] = 'medium'
        elif 3000 <= int(data['capital-loss'][i]) < 4000:
            data['capital-loss'][i] = 'high'
        else:
            data['capital-loss'][i] = 'very high'
#function below is for coverting capital-gain numbers to names
def capital_gain_modification(data):
    for i in range(len(data)):
        if int(data['capital-gain'][i]) < 20000:
            data['capital-gain'][i] = 'very low'
        elif 20000 <= int(data['capital-gain'][i]) < 40000:
            data['capital-gain'][i] = 'low'
        elif 4000 <= int(data['capital-gain'][i]) < 60000:
            data['capital-gain'][i] = 'medium'
        elif 60000 <= int(data['capital-gain'][i]) < 8000:
            data['capital-gain'][i] = 'high'
        else:
            data['capital-gain'][i] = 'very high'
#function below is for coverting eduacation_num numbers to names
def eduaction_num_modification(data):
    for i in range(len(data)):
        if int(data['education-num'][i]) <= 4:
            data['education-num'][i] = 'first quarter'
        elif 4 < int(data['education-num'][i]) <= 8:
            data['education-num'][i] = 'second querter'
        elif 8 < int(data['education-num'][i]) <=12:
            data['education-num'][i] = 'third quarter'
        else:
            data['education-num'][i] = 'last quarter'
#function below is for coverting fnlwgt numbers to names
def fnlwgt_modification(data):
    for i in range(len(data)):
        if int(data['fnlwgt'][i]) < 25000:
            data['fnlwgt'][i] = 'very low'
        elif 25000 <= int(data['fnlwgt'][i]) < 50000:
            data['fnlwgt'][i] = 'low'
        elif 50000 <= int(data['fnlwgt'][i]) < 75000:
            data['fnlwgt'][i] = 'medium'
        elif 75000 <= int(data['fnlwgt'][i]) < 100000:
            data['fnlwgt'][i] = 'high'
        else:
            data['fnlwgt'][i] = 'very high'
#function below is for modification all numerical attributes for known data 
def data_pre_processing(data,mode):
    if mode == 'known':
        age_modification(data)
        income_modification(data)
        hour_modification(data)
        capital_loss_modification(data)
        capital_gain_modification(data)
        eduaction_num_modification(data)
        fnlwgt_modification(data)
    elif mode == 'unknown':
        age_modification(data)
        hour_modification(data)
        capital_loss_modification(data)
        capital_gain_modification(data)
        eduaction_num_modification(data)
        fnlwgt_modification(data)
    else:
        print('unsupported mode')
#reading and pre-processing known data
knownData = pd.read_csv('Dataset1.csv')
unknownData = pd.read_csv('Dataset1_Unknown.csv')
data_pre_processing(knownData,mode = 'known')
data_pre_processing(unknownData, mode = 'unknown') 
#saving modified known data
pickle.dump(knownData,open('knownP1','wb'))
pickle.dump(unknownData,open('unknownP1','wb'))