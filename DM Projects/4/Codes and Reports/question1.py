"""
Created on Sun Jan  2 21:13:43 2022

@author: mcaptain79
"""
import random
import pandas as pd
import math
import matplotlib.pyplot as plt
#reading data
data = pd.read_csv('Dataset1.csv')
#function below is for initializing random centres from points and saving data in array
dataArray = []
for i in range(len(data)):
    dataArray.append((data.iloc[i][0],data.iloc[i][1]))
def initialize_centres(data,clusterNumber):
    centres = random.choices(data,k = clusterNumber)
    return centres
#function below is for calculating distance between two points
def distance(dot1,dot2):
    return math.sqrt((dot1[0]-dot2[0])**2+(dot1[1]-dot2[1])**2)
#function below is for calculating which data belong to which centre
""" 
clusters form
            [[(),(),()],
             [(),()],
             [(),()],
             [(),(),(),()]]
"""
def findClosestCentres(data,centres):
    clusters = []
    #each cluster at first just have centers in it
    for i in range(len(centres)):
        clusters.append([centres[i],])
    for i in range(len(data)):
        #at first we assume minimum distance is with first centre and we will update it later
        minDist = distance(data[i],centres[0])
        minimum = 0
        for j in range(len(centres)):
            dist = distance(data[i], centres[j])
            if dist < minDist:
                minDist = dist
                minimum = j
        clusters[minimum].append(data[i])
    for i in range(len(centres)):
        clusters[i].pop(0)
    return clusters
#function to compute centres
def computeMeans(data,clusters,clusterNumber):
    centres = []
    for i in range(clusterNumber):
        xSum = 0
        ySum = 0
        for j in range(len(clusters[i])):
            xSum += clusters[i][j][0]
            ySum += clusters[i][j][1]
        centres.append((xSum/len(clusters[i]),(ySum/len(clusters[i]))))
    return centres
#function below is for for main algorithm
def k_means(data,clusterNumber):
    centres = initialize_centres(data, clusterNumber)
    for i in range(15):
        clusters = findClosestCentres(data, centres)
        centres = computeMeans(data, clusters, clusterNumber)
    return clusters
#computing kmeans on 2 clusters
k2means = k_means(dataArray,2)
#plotting clusters
x1_k2means = []
y1_k2means = []
x2_k2means = []
y2_k2means = []
for i in range(len(k2means[0])):
    x1_k2means.append(k2means[0][i][0])
    y1_k2means.append(k2means[0][i][1])
for i in range(len(k2means[1])):
    x2_k2means.append(k2means[1][i][0])
    y2_k2means.append(k2means[1][i][1])
plt.scatter(x1_k2means,y1_k2means,color = 'blue')
plt.scatter(x2_k2means,y2_k2means,color = 'red')
plt.show()
#computing kmeans on 3 clusters
k3means = k_means(dataArray,3)
#plotting clusters
x1_k3means = []
y1_k3means = []
x2_k3means = []
y2_k3means = []
x3_k3means = []
y3_k3means = []
for i in range(len(k3means[0])):
    x1_k3means.append(k3means[0][i][0])
    y1_k3means.append(k3means[0][i][1])
for i in range(len(k3means[1])):
    x2_k3means.append(k3means[1][i][0])
    y2_k3means.append(k3means[1][i][1])
for i in range(len(k3means[2])):
    x3_k3means.append(k3means[2][i][0])
    y3_k3means.append(k3means[2][i][1])
plt.scatter(x1_k3means,y1_k3means,color = 'blue')
plt.scatter(x2_k3means,y2_k3means,color = 'red')
plt.scatter(x3_k3means,y3_k3means,color = 'green')
plt.show()
#computing kmeans on 4 clusters
k4means = k_means(dataArray,4)
#plotting clusters
x1_k4means = []
y1_k4means = []
x2_k4means = []
y2_k4means = []
x3_k4means = []
y3_k4means = []
x4_k4means = []
y4_k4means = []
for i in range(len(k4means[0])):
    x1_k4means.append(k4means[0][i][0])
    y1_k4means.append(k4means[0][i][1])
for i in range(len(k4means[1])):
    x2_k4means.append(k4means[1][i][0])
    y2_k4means.append(k4means[1][i][1])
for i in range(len(k4means[2])):
    x3_k4means.append(k4means[2][i][0])
    y3_k4means.append(k4means[2][i][1])
for i in range(len(k4means[3])):
    x4_k4means.append(k4means[3][i][0])
    y4_k4means.append(k4means[3][i][1])
plt.scatter(x1_k4means,y1_k4means,color = 'blue')
plt.scatter(x2_k4means,y2_k4means,color = 'red')
plt.scatter(x3_k4means,y3_k4means,color = 'green')
plt.scatter(x4_k4means,y4_k4means,color = 'yellow')
plt.show()
        