"""
Created on Wed Oct 27 20:13:27 2021

@author: mcaptain79
"""
import numpy as np
import random
import matplotlib.pyplot as plt
myData = np.load('data.npz')
#loading parameters in np array
x1 = myData['x1']
x2 = myData['x2']
y = myData['y']
x1_test = myData['x1_test']
x2_test = myData['x2_test']
y_test = myData['y_test']
"""
y = B0 + B1*x1 + B2*x2
we should find best Bi combination to fit our data using regression
"""
#initialize B0,B1,B2 to zero and finding best value later
B = np.array([[1],[1],[1]])
oneMatrix = np.full((len(x1),1),1)
#creating X matrix
X = np.concatenate((oneMatrix,x1.reshape(len(x1),1),x2.reshape(len(x2),1)),axis = 1)
#algorithm nelow is for training values of B using batch gradient desent
for i in range(50):
    B_gradient = np.transpose(X)@X@B - np.transpose(X)@y.reshape(len(y),1)
    B = B - 0.01*B_gradient
print('B in batch gradient desent')
print(B)
print('---------------------------------------------------')
#algorithm below is for stochastic gradient desent
B2 = np.array([[1],[1],[1]])
for i in range(300):
    random_number = random.randint(0, len(x1)-1)
    XTWO = np.array([[1,x1[random_number],x2[random_number]]])
    B2_gradient = np.transpose(XTWO)@XTWO@B2 - 0.1*np.transpose(XTWO)*y[random_number]
    B2 = B2 - 0.01*B2_gradient
print('B in stochastic gradient desnt')
print(B2)
#plotting test data real value and gradient desnt and stochastic
print('---------------------------------------------')
X_grad = np.concatenate((np.full((len(x1_test),1), 1),x1_test.reshape(len(x1_test),1),
                         x2_test.reshape(len(x2_test),1)),axis = 1)
y_gradient = X_grad@B
y_stochastic = X_grad@B2
ax = plt.axes(projection='3d')
ax.plot3D(y_test,y_gradient.reshape(len(y_gradient)),y_stochastic.reshape(len(y_stochastic)))
plt.show()
print('-----------------------------------------')
#code below is for calculating the error
def error(arr1,arr2):
    length = len(arr1)
    totalErr = 0
    for i in range(length):
        totalErr += (arr1[i]-arr2[i])**2
    return totalErr
#for training data set
y_grad_train = X@B 
y_stoch_train = X@B2
print('train')
print('err for grad desent:',error(y,y_grad_train.reshape(len(y_grad_train)))
      ,'err for stochastic:',error(y,y_stoch_train.reshape(len(y_stoch_train))))
print('test')
print('err for grad desent:',error(y_test,y_gradient.reshape(len(y_gradient)))
      ,'err for stochastic:',error(y_test,y_stochastic.reshape(len(y_stochastic))))
   
