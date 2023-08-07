"""
Created on Wed Oct 27 20:13:29 2021

@author: mcaptain79
"""
import pandas as pd
import matplotlib.pyplot as plt
#a
myData = pd.read_csv('players.csv')
print('---------------------PART A----------------------------------------')
print('first 5 data')
print(myData[:5])
print('last 5 data')
print(myData[len(myData)-5:len(myData)])
#b
print('---------------------PART B----------------------------------------')
print(myData.isnull())
#c
print('---------------------PART C----------------------------------------')
print('min',min(myData['Weight']))
print('max',max(myData['Weight']))
print('mean',sum(myData['Weight'])/len(myData['Weight']))
#d
print('---------------------PART D----------------------------------------')
counts = myData['Nationality'].value_counts()
print('max:',counts[0:1],'\nmin:',counts[len(counts)-1:len(counts)])
#e
print('---------------------PART E----------------------------------------')
positions = {'CB':0,'GK':0,'ST':0,'CDM':0,'CM':0,'RB':0,'LB':0,'LM':0,'LWB':0,'CAM':0}
def updatePositions(pos_arg):
    for i in positions:
        if i in pos_arg.split(','):
            positions[i] += 1
for i in range(len(myData)):
    if myData['Growth'][i] < 3 and myData['Potential'][i] < 84:
        print('palyer name:',myData['FullName'][i],'Growth:',myData['Growth'][i],
             'Potential:',myData['Potential'][i])
        pos = myData['Positions'][i]
        updatePositions(pos)
#f
print('---------------------PART F----------------------------------------')
plt.bar(positions.keys(),positions.values())
plt.show()
#g
print('---------------------PART G----------------------------------------')
newData = myData[(myData['Potential'] > 80) & (myData['Age'] < 24)]
clubCounts = newData['Club'].value_counts()
print('max:',clubCounts[0:1])
print('min',clubCounts[len(clubCounts)-1:len(clubCounts)])
#h
print('---------------------PART H----------------------------------------')
counter = 0
for i in range(len(myData)):
    if myData['ContractUntil'][i] == 2021 and myData['NationalTeam'][i] == 'Not in team':
        counter += 1
print(counter)
#i
print('---------------------PART I----------------------------------------')
for i in range(len(myData)):
    if myData['Club'][i] == 'Chelsea' and myData['Age'][i] < 24:
        print('name:',myData['FullName'][i],'value:',myData['ValueEUR'][i])
#j
print('---------------------PART J----------------------------------------')
for i in range(len(myData)):
    if myData['Name'][i] == 'E. Hazard':
        print('Positions:',myData['Positions'][i],'income:',myData['WageEUR'][i],
              'Club',myData['Club'][i])
        break