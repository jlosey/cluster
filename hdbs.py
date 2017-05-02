
#!/usr/bin/env python
import numpy as np
from sklearn import metrics
import hdbscan 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Read in cluster data
cols = [] 
f = open('lj-rho-0.2.temp-1.0.xyz','r')
for line in f:
 	li=line.strip()
	if not li.startswith("1000") and not li.startswith("Atoms"):
		x = li.split()
		cols.append([float(x[1]),float(x[2]),float(x[3])])

f.close()
coord = np.asarray(cols)
coordFr = coord[5000:6000]
#print coord[1000]
scr = []
neighb = []
#Run DBSCAN clustering algorithm for first dump
hdb_labels = hdbscan.HDBSCAN(min_cluster_size=4).fit_predict(coordFr[:])
#hierarchy = hdbscan.cluster_hierarchy_
#print hierarchy
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
ax.scatter(coordFr[:,0], coordFr[:, 1], coordFr[:, 2], c=hdb_labels.astype(np.float), s=200)
#ax.scatter(coord[4000:5000,0], coord[4000:5000, 1], coord[4000:5000, 2], s=200)
plt.show()

