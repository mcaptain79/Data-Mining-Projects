"""
Created on Fri Dec  3 21:03:30 2021

@author: mcaptain79
"""
import pickle 
from sklearn import tree
#importing lable encoder for coverting so dtree can work properly
from sklearn.preprocessing import LabelEncoder
#reading data using pickle
knownData = pickle.load(open('knownP1','rb'))
unknownData = pickle.load(open('unknownP1','rb'))
#adding income column to unknown data
unknownData['income'] = ['N']*6512
#using lable encoder for known and unknown data
lb = LabelEncoder()
for i in knownData:
    knownData[i] = lb.fit_transform(knownData[i])
    unknownData[i] = lb.fit_transform(unknownData[i])
#splitting knownData to train and test 20839 data is for train and rest for test
trainData = knownData[:20839]
testData = knownData[20839:len(knownData)]
#creating two tress one for gini and one for entropy
decisionTree1 = tree.DecisionTreeClassifier(criterion = 'gini')
decisionTree2 = tree.DecisionTreeClassifier(criterion = 'entropy')
#saving features names
features = ['age','workclass','fnlwgt','education','education-num','marital-status',
            'occupation','relationship','race','sex','capital-gain','capital-loss',
            'hours-per-week','native-country']
#learning decition tree 1 and 2
decisionTree1.fit(trainData[features],trainData['income'])
decisionTree2.fit(trainData[features],trainData['income'])
#preciting y and calculating accuracy
accuracy1 = 0
accuracy2 = 0
for i in range(len(testData)):
    predicted1 = decisionTree1.predict([testData[features].iloc[i]])
    predicted2 = decisionTree2.predict([testData[features].iloc[i]])
    real = testData['income'].iloc[i]
    if predicted1[0] == real:
        accuracy1 += 1
    if predicted2[0] == real:
        accuracy2 += 1
print('accuracy using gini:',accuracy1/len(testData))
print('accuracy using entropy:',accuracy2/len(testData))
#predicting unknown data using tree2
for i in range(len(unknownData)):
    predicted = decisionTree2.predict([unknownData[features].iloc[i]])
    unknownData['income'][i] = predicted
print(unknownData)