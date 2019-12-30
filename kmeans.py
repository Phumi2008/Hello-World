#K-Means clustering implementation

#Some hints on how to start have been added to this file.
#You will have to add more code that just the hints provided here for the full implementation.
import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv
import sys

# ====
# Define a function that computes the distance between two data points
def distance(p1, p2): 
    return np.sum((p1 - p2)**2) 

# ====
# Define a function that reads data in from the csv files  HINT: http://docs.python.org/2/library/csv.html
data = input("Please enter choose the data file you want to download 'data2008.csv','data1953.csv','dataBoth.csv'")
             
dataset = pd.read_csv(data)
dataset.describe()
print (dataset)

# ====
# Write the initialisation procedure
X = dataset.iloc[:, [1, 2]].values
m=X.shape[0] #number of training examples
n=X.shape[1] #number of features.Here n=2
n_iter = int(input("please enter the number of iteration"))
K = int(input("Please enter the number of clusters"))
Centroids=np.array([]).reshape(n,0)
for i in range(K):
    rand=rd.randint(0,m-1)
    Centroids=np.c_[Centroids,X[rand]]
# ====
# Implement the k-means algorithm, using appropriate looping
# calculate the euclidian distance from each point to all the cetnriods
# store them in X K matrics
# STEP 2a
Output={}  # results/output will be a dictionary with cluster numbers as keys and data points as values
EuclidianDistance=np.array([]).reshape(m,0)
for k in range(K):
       tempDist=np.sum((X-Centroids[:,k])**2,axis=1)
       EuclidianDistance=np.c_[EuclidianDistance,tempDist]
C=np.argmin(EuclidianDistance,axis=1)+1 #find the minimum distance and store the index of the column in a vector C

#Regrouping the data points based on the cluster index C and store in the Output dictionary
#STEP 2b
Y={} #Temporary dictionary which stores the results for one particular iteration.
for k in range(K):
    Y[k+1]=np.array([]).reshape(2,0)
    
for i in range(m):
    Y[C[i]]=np.c_[Y[C[i]],X[i]]
     
for k in range(K):
    Y[k+1]=Y[k+1].T
    
for k in range(K):
     Centroids[:,k]=np.mean(Y[k+1],axis=0)

# loop over n_iter repeat steps 2a and 2b till convergence is achieved
for i in range(n_iter):
     #step 2.a
      EuclidianDistance=np.array([]).reshape(m,0)
      for k in range(K):
          tempDist=np.sum((X-Centroids[:,k])**2,axis=1)
          EuclidianDistance=np.c_[EuclidianDistance,tempDist]
      C=np.argmin(EuclidianDistance,axis=1)+1
     #step 2.b
      Y={}
      for k in range(K):
          Y[k+1]=np.array([]).reshape(2,0)
      for i in range(m):
          Y[C[i]]=np.c_[Y[C[i]],X[i]]
     
      for k in range(K):
          Y[k+1]=Y[k+1].T
    
      for k in range(K):
          Centroids[:,k]=np.mean(Y[k+1],axis=0)
      Output=Y     # Results

# ====
# Print out the results

color=['red','blue','green','cyan','magenta']
labels=['cluster1','cluster2','cluster3','cluster4','cluster5']
for k in range(K):
    plt.scatter(Output[k+1][:,0],Output[k+1][:,1],c=color[k],label=labels[k])
plt.scatter(Centroids[0,:],Centroids[1,:],s=300,c='yellow',label='Centroids')
plt.xlabel('BirthRate(Per1000 - 2008)')
plt.ylabel('LifeExpectancy(2008)')
plt.legend()
plt.show()

# function for printing clusters

dataset['Cls'] = C
print ('Cls')


df0 = dataset.groupby('Cls').mean()
print(df0)

df1 = dataset.groupby('Cls').count()
print(df1)

df2 = dataset.groupby('Cls')['Countries']
for key,items in df2:
    print(items.to_string())
    print()




#TASK 2 (KMean ++)
#===================    

#Randomly select the first cluster center from the data points and append it to the centroid matrix
    
i=rd.randint(0,X.shape[0])
Centroid=np.array([X[i]])

# number of cluster chosen by users
K = int(input("Please enter the number of clusters"))
                     
#Loop over the number of Centroids that need to be chosen (K)
for k in range(1,K):
    # for each data point calculate the euclidian distance square from already chosen centroids
    # append the minimum distance to a Distance array
    D=np.array([]) 
    for x in X:
        D=np.append(D,np.min(np.sum((x-Centroid)**2),axis=0))
        
#Calculate the probabilities of choosing the particular data
#point as the next centroid by dividing the Distance array elements with the sum of Distance array
        
    prob=D/np.sum(D)
    
#Calculate the cumulative probability distribution from prob

    cummulative_prob=np.cumsum(prob)

# Select a random number between 0 to 1, get the index (i) of the cumulative probability distribution (cumulative_prob)
#which is just greater than the chosen random number and assign the data point corresponding to the selected index (i).  
    r=rd.random()
    i=0
    for j,p in enumerate(cummulative_prob):
        if r<p:
            i=j
            break
    Centroid=np.append(Centroid,[X[i]],axis=0)
    print(Centroid) #printing the results to monitors convergence

#NB: I noted the suggested code for Kmean ++ , I understand this one better and can explain it.
