"""
Created on Sat Nov 27 22:40:30 2021

@author: mcaptain79
"""
import pandas as pd
knownData = pd.read_csv('Dataset3.csv')
unknownData = pd.read_csv('Dataset3_Unknown.csv')
#functions below is for converting numeric data to names
def modify_age(data):
    for i in range(len(data)):
        if int(data['age'][i]) <= 20:
            data['age'][i] = 'A'
        elif 20 < int(data['age'][i]) <= 40:
            data['age'][i] = 'B'
        elif 40 < int(data['age'][i]) <= 60:
            data['age'][i] = 'C'
        else:
            data['age'][i] = 'D'
def modify_sex(data):
    for i in range(len(data)):
        if int(data['sex'][i]) == 0:
            data['sex'][i] = 'female'
        else:
            data['sex'][i] = 'male'
def modify_cp(data):
    for i in range(len(data)):
        if int(data['cp'][i]) == 0:
            data['cp'][i] = 'cp0'
        elif int(data['cp'][i]) == 1:
            data['cp'][i] = 'cp1'
        elif int(data['cp'][i]) == 2:
            data['cp'][i] = 'cp2'
        else:
            data['cp'][i] = 'cp3'
def modify_trestbps(data):
    for i in range(len(data)):
        if int(data['trestbps'][i]) <= 130:
            data['trestbps'][i] = 'very low'
        elif 130 < int(data['trestbps'][i]) <= 150:
            data['trestbps'][i] = 'low'
        elif 150 < int(data['trestbps'][i]) <= 160:
            data['trestbps'][i] = 'medium'
        else:
            data['trestbps'][i] = 'high'
def modify_chol(data):
    for i in range(len(data)):
        if int(data['chol'][i]) <= 150:
            data['chol'][i] = 'very low'
        elif 150 < int(data['chol'][i]) <= 300:
            data['chol'][i] = 'low'
        elif 300 < int(data['chol'][i]) <= 450:
            data['chol'][i] = 'medium'
        else:
            data['chol'][i] = 'high'
def modify_fbs(data):
    for i in range(len(data)):
        if int(data['fbs'][i]) == 0:
            data['fbs'][i] = 'zero'
        else:
            data['fbs'][i] = 'one'
def modify_restecg(data):
    for i in range(len(data)):
        if int(data['restecg'][i]) == 0:
            data['restecg'][i] = 'restecg0'
        elif int(data['restecg'][i]) == 1:
            data['restecg'][i] = 'restecg1'
        else:
            data['restecg'][i] = 'restecg2'
def modify_thalach(data):
    for i in range(len(data)):
        if int(data['thalach'][i]) <= 90:
            data['thalach'][i] = 'very low'
        elif 90 < int(data['thalach'][i]) <= 120:
            data['thalach'][i] = 'low'
        elif 120 < int(data['thalach'][i]) <= 150:
            data['thalach'][i] = 'medium'
        else:
            data['thalach'][i] = 'high'
def modify_exang(data):
    for i in range(len(data)):
        if int(data['exang'][i]) == 0:
            data['exang'][i] = 'zero'
        else:
            data['exang'][i] = 'one'
def modify_oldpeak(data):
    for i in range(len(data)):
        if float(data['oldpeak'][i]) <= 1.25:
            data['oldpeak'][i] = 'very low'
        elif 1.25 < float(data['oldpeak'][i]) <= 2.5:
            data['oldpeak'][i] = 'low'
        elif 2.5 < float(data['oldpeak'][i]) <= 3.75:
            data['oldpeak'][i] = 'medium'
        else:
            data['oldpeak'][i] = 'high'
def modify_slope(data):
    for i in range(len(data)):
        if int(data['slope'][i]) == 0:
            data['slope'][i] = 'slope0'
        elif int(data['slope'][i]) == 1:
            data['slope'][i] = 'slope1'
        else:
            data['slope'][i] = 'slope2'
def modify_ca(data):
    for i in range(len(data)):
        if int(data['ca'][i]) == 0:
            data['ca'][i] = 'ca0'
        elif int(data['ca'][i]) == 1:
            data['ca'][i] = 'ca1'
        elif int(data['ca'][i]) == 2:
            data['ca'][i] = 'ca2'
        elif int(data['ca'][i]) == 3:
            data['ca'][i] = 'ca3'
        else:
            data['ca'][i] = 'ca4'
def modify_thal(data):
    for i in range(len(data)):
        if int(data['thal'][i]) == 0:
            data['thal'][i] = 'thal0'
        elif int(data['thal'][i]) == 1:
            data['thal'][i] = 'thal1'
        elif int(data['thal'][i]) == 2:
            data['thal'][i] = 'thal2'
        else:
            data['thal'][i] = 'thal3'
def modify_disease(data):
    for i in range(len(data)):
        if int(data['disease'][i]) == 1:
            data['disease'][i] = 'y'
        else:
            data['disease'][i] = 'n'
def modify_data(data,mode):
    modify_age(data)
    modify_ca(data)
    modify_chol(data)
    modify_cp(data)
    modify_exang(data)
    modify_fbs(data)
    modify_oldpeak(data)
    modify_restecg(data)
    modify_sex(data)
    modify_slope(data)
    modify_thal(data)
    modify_thalach(data)
    modify_trestbps(data)
    if mode == 'known':
        modify_disease(data)
#modifying our data
modify_data(knownData, 'known')
modify_data(unknownData, 'unknown')
#adding new disese column to unknown data
unknownData['disease'] = ['u']*len(unknownData)
#193 of known data item is for training the rest is for testing
#below dictionaries are for calculating p for naive bayes
#calculating probality of disease y or n
diseaseCount = knownData['disease'][:193].value_counts()
print(diseaseCount)
print('----------------------------------')
diseasePositiveNum = diseaseCount[0]
diseaseNegativeNum = diseaseCount[1]
p_diseasePositive = diseaseCount[0]/193
p_diseaseNegative = diseaseCount[1]/193
#calculating p(coulumn|disease) in dictionary the form is {(column,diseaseStatus):count/len}
ageCount = knownData[:193].groupby(['age','disease']).size()
print(ageCount)
p_age = {('A','y'):0,('A','n'):0,('B','y'):11/diseasePositiveNum,('B','n'):1/diseaseNegativeNum,('C','y'):96/diseasePositiveNum,('C','n'):35/diseaseNegativeNum,('D','y'):31/diseasePositiveNum,('D','n'):19/diseaseNegativeNum}
print('----------------------------------')
sexCount = knownData[:193].groupby(['sex','disease']).size()
print(sexCount)
p_sex = {('female','y'):61/diseasePositiveNum,('female','n'):8/diseaseNegativeNum,('male','y'):77/diseasePositiveNum,('male','n'):47/diseaseNegativeNum}
print('---------------------------------------------------')
cp_count = knownData[:193].groupby(['cp','disease']).size()
print(cp_count)
p_cp = {('cp0','y'):31/diseasePositiveNum,('cp0','n'):40/diseaseNegativeNum,('cp1','y'):34/diseasePositiveNum,('cp1','n'):3/diseaseNegativeNum,
        ('cp2','y'):60/diseasePositiveNum,('cp2','n'):10/diseaseNegativeNum,('cp3','y'):13/diseasePositiveNum,('cp3','n'):2/diseaseNegativeNum}
print('---------------------------------------------------')
trestbps_count = knownData[:193].groupby(['trestbps','disease']).size()
print(trestbps_count)
p_trestbps = {('very low','y'):80/diseasePositiveNum,('very low','n'):31/diseaseNegativeNum,
              ('low','y'):47/diseasePositiveNum,('low','n'):19/diseaseNegativeNum,
              ('medium','y'):7/diseasePositiveNum,('medium','n'):3/diseaseNegativeNum,
              ('high','y'):4/diseasePositiveNum,('high','n'):2/diseaseNegativeNum}
print('---------------------------------------------------')
chol_count = knownData[:193].groupby(['chol','disease']).size()
print(chol_count)
p_chol = {('very low','y'):3/diseasePositiveNum,('very low','n'):0/diseaseNegativeNum,
              ('low','y'):114/diseasePositiveNum,('low','n'):46/diseaseNegativeNum,
              ('medium','y'):20/diseasePositiveNum,('medium','n'):9/diseaseNegativeNum,
              ('high','y'):1/diseasePositiveNum,('high','n'):0/diseaseNegativeNum}
print('---------------------------------------------------')
fbs_count = knownData[:193].groupby(['fbs','disease']).size()
print(fbs_count)
p_fbs = {('one','y'):18/diseasePositiveNum,('one','n'):7/diseaseNegativeNum,('zero','y'):120/diseasePositiveNum,('zero','n'):48/diseaseNegativeNum}
print('---------------------------------------------------')
restecg_count = knownData[:193].groupby(['restecg','disease']).size()
p_restecg = {('restecg0','y'):55/diseasePositiveNum,('restecg0','n'):36/diseaseNegativeNum,('restecg1','y'):82/diseasePositiveNum,('restecg1','n'):19/diseaseNegativeNum,
        ('restecg2','y'):1/diseasePositiveNum,('restecg2','n'):0/diseaseNegativeNum}
print(restecg_count)
print('---------------------------------------------------')
thalach_count = knownData[:193].groupby(['thalach','disease']).size()
print(thalach_count)
p_thalach = {('very low','y'):0/diseasePositiveNum,('very low','n'):0/diseaseNegativeNum,
              ('low','y'):6/diseasePositiveNum,('low','n'):11/diseaseNegativeNum,
              ('medium','y'):30/diseasePositiveNum,('medium','n'):22/diseaseNegativeNum,
              ('high','y'):102/diseasePositiveNum,('high','n'):22/diseaseNegativeNum}
print('---------------------------------------------------')
exang_count = knownData[:193].groupby(['exang','disease']).size()
print(exang_count)
p_exang = {('one','y'):20/diseasePositiveNum,('one','n'):29/diseaseNegativeNum,('zero','y'):118/diseasePositiveNum,('zero','n'):26/diseaseNegativeNum}
print('---------------------------------------------------')
oldpeak_count = knownData[:193].groupby(['oldpeak','disease']).size()
print(oldpeak_count)
p_oldpeak = {('very low','y'):114/diseasePositiveNum,('very low','n'):21/diseaseNegativeNum,
              ('low','y'):20/diseasePositiveNum,('low','n'):17/diseaseNegativeNum,
              ('medium','y'):3/diseasePositiveNum,('medium','n'):14/diseaseNegativeNum,
              ('high','y'):1/diseasePositiveNum,('high','n'):3/diseaseNegativeNum}
print('---------------------------------------------------')
slope_count = knownData[:193].groupby(['slope','disease']).size()
print(slope_count)
p_slope = {('slope0','y'):7/diseasePositiveNum,('slope0','n'):8/diseaseNegativeNum,('slope1','y'):39/diseasePositiveNum,('slope1','n'):34/diseaseNegativeNum,
        ('slope2','y'):92/diseasePositiveNum,('slope2','n'):13/diseaseNegativeNum}
print('---------------------------------------------------')
ca_count = knownData[:193].groupby(['ca','disease']).size()
print(ca_count)
p_ca = {('ca0','y'):107/diseasePositiveNum,('ca0','n'):20/diseaseNegativeNum,('ca1','y'):18/diseasePositiveNum,('ca1','n'):18/diseaseNegativeNum,
        ('ca2','y'):7/diseasePositiveNum,('ca2','n'):12/diseaseNegativeNum,('ca3','y'):4/diseasePositiveNum,('ca3','n'):0/diseaseNegativeNum}
print('---------------------------------------------------')
thal_count = knownData[:193].groupby(['thal','disease']).size()
print(thal_count)
p_thal = {('thal1','y'):3/diseasePositiveNum,('thal1','n'):3/diseaseNegativeNum,
        ('thal2','y'):113/diseasePositiveNum,('thal2','n'):10/diseaseNegativeNum,
        ('thal3','y'):22/diseasePositiveNum,('thal3','n'):42/diseaseNegativeNum,
        ('thal0','y'):0/diseasePositiveNum,('thal0','n'):0/diseaseNegativeNum}
print('---------------------------------------------------')
#function below is for calculating accuracy
def accuracy_calc(data,start,end):
    accuracy = 0
    for i in range(start,end):
        disease_y = p_diseasePositive*(p_age[(data['age'][i],'y')]+0.001)*(p_sex[(data['sex'][i],'y')]+0.001)*(p_cp[(data['cp'][i],'y')]+0.001)*(p_trestbps[(data['trestbps'][i],'y')]+0.001)*(p_chol[(data['chol'][i],'y')]+0.001)*(p_fbs[(data['fbs'][i],'y')]+0.001)*(p_restecg[(data['restecg'][i],'y')]+0.001)*(p_thalach[(data['thalach'][i],'y')]+0.001)*(p_exang[(data['exang'][i],'y')]+0.001)*(p_oldpeak[(data['oldpeak'][i],'y')]+0.001)*(p_slope[(data['slope'][i],'y')]+0.001)*(p_thal[(data['thal'][i],'y')]+0.001)
        disease_n = p_diseaseNegative*(p_age[(data['age'][i],'n')]+0.001)*(p_sex[(data['sex'][i],'n')]+0.001)*(p_cp[(data['cp'][i],'n')]+0.001)*(p_trestbps[(data['trestbps'][i],'n')]+0.001)*(p_chol[(data['chol'][i],'n')]+0.001)*(p_fbs[(data['fbs'][i],'n')]+0.001)*(p_restecg[(data['restecg'][i],'n')]+0.001)*(p_thalach[(data['thalach'][i],'n')]+0.001)*(p_exang[(data['exang'][i],'n')]+0.001)*(p_oldpeak[(data['oldpeak'][i],'n')]+0.001)*(p_slope[(data['slope'][i],'n')]+0.001)*(p_thal[(data['thal'][i],'n')]+0.001)
        predictedLable = 'n'
        if disease_y > disease_n:
            predictedLable = 'y'
        if predictedLable == data['disease'][i]:
            accuracy += 1
    return accuracy/(len(data)-193)
print('accuracy: ',accuracy_calc(knownData,193,len(knownData)))
print('--------------------------------------------------')
#algothm below is for predicting new data
def predict_data_lable(data):
    for i in range(len(data)):
        disease_y = p_diseasePositive*(p_age[(data['age'][i],'y')]+0.001)*(p_sex[(data['sex'][i],'y')]+0.001)*(p_cp[(data['cp'][i],'y')]+0.001)*(p_trestbps[(data['trestbps'][i],'y')]+0.001)*(p_chol[(data['chol'][i],'y')]+0.001)*(p_fbs[(data['fbs'][i],'y')]+0.001)*(p_restecg[(data['restecg'][i],'y')]+0.001)*(p_thalach[(data['thalach'][i],'y')]+0.001)*(p_exang[(data['exang'][i],'y')]+0.001)*(p_oldpeak[(data['oldpeak'][i],'y')]+0.001)*(p_slope[(data['slope'][i],'y')]+0.001)*(p_thal[(data['thal'][i],'y')]+0.001)
        disease_n = p_diseaseNegative*(p_age[(data['age'][i],'n')]+0.001)*(p_sex[(data['sex'][i],'n')]+0.001)*(p_cp[(data['cp'][i],'n')]+0.001)*(p_trestbps[(data['trestbps'][i],'n')]+0.001)*(p_chol[(data['chol'][i],'n')]+0.001)*(p_fbs[(data['fbs'][i],'n')]+0.001)*(p_restecg[(data['restecg'][i],'n')]+0.001)*(p_thalach[(data['thalach'][i],'n')]+0.001)*(p_exang[(data['exang'][i],'n')]+0.001)*(p_oldpeak[(data['oldpeak'][i],'n')]+0.001)*(p_slope[(data['slope'][i],'n')]+0.001)*(p_thal[(data['thal'][i],'n')]+0.001)
        if disease_y > disease_n:
            data['disease'][i] = 'y'
        else:
            data['disease'][i] = 'n'
predict_data_lable(unknownData)
print(unknownData)