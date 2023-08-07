"""
Created on Thu Nov 25 20:57:35 2021

@author: mcaptain79
"""
import pandas as pd
import matplotlib.pyplot as plt
import sys
#reading data from data sets
knownData = pd.read_csv('Dataset2.csv')
unknownData = pd.read_csv('Dataset2_Unknown.csv')
#function below is for calculating similarity between two rows
def similarity_calculate(data,i,j):
    similarity = 0
    for k in data:
        if data.loc[i][k] == data.loc[j][k]:
            similarity += 1
    return similarity
#function below is for predicting a lable
def predict_lable(saveList,k):
    e = 0
    p = 0
    for i in range(len(saveList)-k,len(saveList)):
        if saveList[i].lable == 'e':
            e += 1
        else:
            p += 1
    if e > p:
        return 'e'
    return 'p'
#class below is for saving lable and similarity
class save():
    def __init__(self,similarity = 0,lable = ''):
        self.similarity = similarity
        self.lable = lable
    def __str__(self):
        return str(self.similarity)+' '+self.lable
    def __lt__(self,obj):
        return self.similarity > obj.similarity
#functions below is for sorting saveList using merge sort
def merge(saveList,start,middle,end):
    n1 = middle-start+1
    n2 = end-middle
    left = []
    right = []
    for i in range(0,n1):
        left.append(saveList[start+i])
    for j in range(0,n2):
        right.append(saveList[middle+j+1])
    left.append(save(sys.maxsize,'e'))
    right.append(save(sys.maxsize,'e')) 
    i = 0
    j = 0
    for k in range(start,end+1):
        if left[i].similarity <= right[j].similarity:
            saveList[k] = left[i]
            i += 1
        else:
            saveList[k] = right[j]
            j += 1
def merge_sort(saveList,start,end):
    if start < end:
        middle = (start+end)//2
        merge_sort(saveList, start, middle)
        merge_sort(saveList, middle+1, end)
        merge(saveList, start, middle, end)
#function below is for testing our knn algorithm
def check_accuracy(data,train_numbers,test_numbers):
    accuracy_k1 = 0
    accuracy_k3 = 0
    accuracy_k5 = 0
    #iterating test data
    for i in range(train_numbers+1,len(data)):
        saveList = []
        for j in range(train_numbers):
            similarity = similarity_calculate(data, i, j)
            lable = data.loc[j]['poisonous']
            saveList.append(save(similarity,lable))
        merge_sort(saveList, 0, len(saveList)-1)
        predictedLable_k1 = predict_lable(saveList, 1)
        predictedLable_k3 = predict_lable(saveList, 3)
        predictedLable_k5 = predict_lable(saveList, 5)
        if predictedLable_k1 == data.loc[i]['poisonous']:
            accuracy_k1 += 1
        if predictedLable_k3 == data.loc[i]['poisonous']:
            accuracy_k3 += 1
        if predictedLable_k5 == data.loc[i]['poisonous']:
            accuracy_k5 += 1
    return accuracy_k1/test_numbers,accuracy_k3/test_numbers,accuracy_k5/test_numbers
accuracy_k1,accuracy_k3,accuracy_k5 = check_accuracy(knownData, 5200, 1299)
print('k = 1','accuracy:',accuracy_k1)
print('k = 3','accuracy:',accuracy_k3)
print('k = 5','accuracy:',accuracy_k5)
#function below is for calculating similarity between two rows of two differnt data sets
def similarity_calculate2(data1,data2,i,j):
    similarity = 0
    for k in data2:
        if data1.loc[i][k] == data2.loc[j][k]: 
            similarity += 1
    return similarity
#function below is for predicting unknown data lables based on known data
def predict(data1,data2,number,k):
    predictList = []
    for i in range(number):
        saveList = []
        for j in range(len(data1)):
            similarity  = similarity_calculate2(data1, data2, j, i)
            lable = data1.loc[j]['poisonous']
            saveList.append(save(similarity,lable))
        merge_sort(saveList,0,len(saveList)-1)
        predictedLable = predict_lable(saveList, k)
        predictList.append(predictedLable)
    return predictList
print('k=1')
print(predict(knownData, unknownData, len(unknownData), 1))
print('---------------------------------------------')
print('k=3')
print(predict(knownData, unknownData, len(unknownData), 3))
print('---------------------------------------------')
print('k=5')
print(predict(knownData, unknownData, len(unknownData), 5))
