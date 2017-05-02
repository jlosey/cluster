
#!/usr/bin/env python
import numpy as np
from sklearn import metrics
from sklearn.cluster import DBSCAN 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Read in cluster data
cols = [] 
f = open('../outputFiles/lj-rho-0.4.temp-1.0.xyz','r')
for line in f:
 	li=line.strip()
	if not li.startswith("1000") and not li.startswith("Atoms"):
		x = li.split()
		cols.append([float(x[1]),float(x[2]),float(x[3])])

f.close()
coord = np.asarray(cols)
#print coord[1000]
scr = []
neighb = []
#Run DBSCAN clustering algorithm for first dump
for n in range(2,18):
	dbscan = DBSCAN(eps=1.5,min_samples=n).fit(coord[4000:5000])
	labels = dbscan.labels_ 
	if sum(labels) <> 0 and sum(labels) <> (len(labels)*-1):
		scoreS = metrics.silhouette_score(coord[4000:5000],labels,metric='euclidean')
		scoreCH =  metrics.calinski_harabaz_score(coord[4000:5000],labels)
		neighb.append(n)
		scr.append([n,scoreS, scoreCH])
scr = np.asarray(scr)
print(scr)
#plt.plot(scr[:,0], scr[:,1], scr[:,0],scr[:,2])
#plt.show()
#plt.clf()
dbscan = DBSCAN(eps=1.5,min_samples=12).fit(coord[4000:5000])
labels = dbscan.labels_
indOut = np.where(labels == -1)
ind0 = np.where(labels == 0)
ind1 = np.where(labels == 1)
ind2 = np.where(labels == 2)
coord0 = coord[4000:5000]
#score = DBSCAN(n_clusters=200, random_state=0).score(coord[:])
#print(kmeans.cluster_centers_)
#print(kmeans2.cluster_centers_)
for n in range(-1,15):
	print(n, sum(1 for x in labels if x==n))
fig = plt.figure(1, figsize=(8, 6))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()
#print labels
#ax.set_xlim3d(0,18)
#ax.set_ylim3d(0,18)
#ax.set_zlim3d(0,18)
#ax.scatter(coord0[indOut,0], coord0[indOut, 1], coord0[indOut, 2], c='green', s=200)
#ax.scatter(coord0[ind0,0], coord0[ind0, 1], coord0[ind0, 2], c='cyan', s=200)
#ax.scatter(coord0[ind1,0], coord0[ind1, 1], coord0[ind1, 2], c='yellow', s=200)
#ax.scatter(coord0[ind2,0], coord0[ind2, 1], coord0[ind2, 2], c='red', s=200)
ax.scatter(coord[4000:5000,0], coord[4000:5000, 1], coord[4000:5000, 2], c=labels.astype(np.float), s=200)
#ax.scatter(coord[4000:5000,0], coord[4000:5000, 1], coord[4000:5000, 2], s=200)
plt.show()

