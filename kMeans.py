
#!/usr/bin/env python
import numpy as np
from sklearn.cluster import AgglomerativeClustering 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Read in cluster data
cols = [] 
f = open('lj-rho-0.4.temp-1.0.xyz','r')
for line in f:
 	li=line.strip()
	if not li.startswith("1000") and not li.startswith("Atoms"):
		x = li.split()
		cols.append([float(x[1]),float(x[2]),float(x[3])])

f.close()
coord = np.asarray(cols)
#print coord[0:1000]
scr = []
#Run KMeans clustering algorithm for first dump
#for n in range(1,100):
#	kmeans = KMeans(n_clusters=n).fit(coord[2000:2999])
#	score = kmeans.score(coord[6000:6999])
	#print(kmeans.cluster_centers_)
#	scr.append([n,score])
clst = AgglomerativeClustering(linkage='Ward', n_clusters=13).fit(coord[3000:3999])
fig = plt.figure(1, figsize=(6, 4.5))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()
labels = clst.labels_
ax.scatter(coord[3000:3999,0], coord[3000:3999, 1], coord[3000:3999, 2], c=labels.astype(np.float), s=200)
plt.show()

#plt.plot(scr)
#plt.show()
