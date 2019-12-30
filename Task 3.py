import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv

dataset = pd.read_csv('data2008.csv')
dataset.describe()
#print (dataset)

X = dataset.iloc[:, [1, 2]].values
m=X.shape[0] #number of training examples
n=X.shape[1]
n_cluster = 3

clf = KMeans(n_clusters=3) # separate data in 3 clusters
clf.fit(X)
predict=clf.predict(X)
# model.fit_predict(data) # combine above two steps in one

#locations of the means generated by the KMeans
centroids = clf.cluster_centers_


# each sample is labelled as well
targets = clf.labels_


# plot the data

dataset['cl'] = predict
print ('cl')

df2 = dataset.groupby('cl')['Countries']
for key,items in df2:
    print(items.to_string())
    print()

df = dataset.groupby('cl').mean()
print(df)


plt.scatter(X[:,0],X[:,1],c= clf.labels_)
plt.scatter(centroids[:, 0],centroids[:, 1],marker='x')
plt.show()

#========================================================

dataset = pd.read_csv('data1953.csv')
dataset.describe()
#print (dataset)

X = dataset.iloc[:, [1, 2]].values
m=X.shape[0] #number of training examples
n=X.shape[1]
n_cluster = 3

clf = KMeans(n_clusters=3) # separate data in 3 clusters
clf.fit(X)
predict=clf.predict(X)
# model.fit_predict(data) # combine above two steps in one

#locations of the means generated by the KMeans
centroids = clf.cluster_centers_


# each sample is labelled as well
targets = clf.labels_


# plot the data

dataset['cl'] = predict
print ('cl')

df = dataset.groupby('cl').mean()
print(df)

df2 = dataset.groupby('cl')['Countries']
for key,items in df2:
    print(items.to_string())
    print()

plt.scatter(X[:,0],X[:,1],c=clf.labels_)
plt.scatter(centroids[:, 0],centroids[:, 1],marker='x')
plt.show()

#========================================================

dataset = pd.read_csv('dataBoth.csv')
dataset.describe()
#print (dataset)

X = dataset.iloc[:, [1, 2]].values
m=X.shape[0] #number of training examples
n=X.shape[1]
n_cluster = 4

clf = KMeans(n_clusters=4) # separate data in 4 clusters
clf.fit(X)
predict=clf.predict(X)
# model.fit_predict(data) # combine above two steps in one

#locations of the means generated by the KMeans
centroids = clf.cluster_centers_


# each sample is labelled as well
targets = clf.labels_


# plot the data

dataset['cl'] = predict
print ('cl')

df = dataset.groupby('cl').mean()
print(df)


df2 = dataset.groupby('cl')['Countries']
for key,items in df2:
    print(items.to_string())
    print()

plt.scatter(X[:,0],X[:,1],c=clf.labels_)
plt.scatter(centroids[:, 0],centroids[:, 1],marker='x')
plt.show()



