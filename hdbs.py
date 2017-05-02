
#!/usr/bin/env python
import numpy as np
from sklearn import metrics
import hdbscan 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Read in cluster data
cols = [] 
f = open('../outputFiles/lj-rho-0.2.temp-1.0.xyz','r')
for line in f:
 	li=line.strip()
	if not li.startswith("1000") and not li.startswith("Atoms"):
		x = li.split()
		cols.append([float(x[1]),float(x[2]),float(x[3])])

f.close()
coord = np.asarray(cols)
coordFr = coord[1000:2000]
#print coord[1000]
scr = []
neighb = []
#Run DBSCAN clustering algorithm for first dump
hdb = hdbscan.HDBSCAN(min_cluster_size=12).fit(coordFr)
hdb_labels = hdb.labels_
prob = hdb.cluster_persistence_
mr,cd = hdbscan.validity.all_points_mutual_reachability(coordFr,hdb_labels,0,metric='euclidean')
#metrics = hdb.dist_metrics_
index0 = np.where(hdb_labels==0)
#hierarchy = clusterer.cluster_hierarchy_
print len(mr),index0
fig = plt.figure(1, figsize=(8, 6))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()	
#print labels
ax.set_xlim3d(0,18)
ax.set_ylim3d(0,18)
ax.set_zlim3d(0,18)
#ax.scatter(coord0[indOut,0], coord0[indOut, 1], coord0[indOut, 2], c='green', s=200)
#ax.scatter(coordFr[index0,0], coordFr[index0, 1], coordFr[index0, 2], c='cyan', s=200)
#ax.scatter(coord0[ind1,0], coord0[ind1, 1], coord0[ind1, 2], c='yellow', s=200)
#ax.scatter(coord0[ind2,0], coord0[ind2, 1], coord0[ind2, 2], c='red', s=200)
ax.scatter(coordFr[:,0], coordFr[:, 1], coordFr[:, 2], c=hdb_labels.astype(np.float), s=200)
plt.show()

