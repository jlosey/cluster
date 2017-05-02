
#!/usr/bin/env python
import numpy as np
impoort debacl as dcl
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
coordF = coord[4000:5000]
tree = dcl.construct_tree(coordF,k=5)
pruned = tree.prune(4)
clust_lbls = pruned.get_clusters()
print "Cluster Labels: ", clust_lbls

print pruned 
plot = pruned.plot()
plot[0].show()
plt.show()
coordClst = coordF[clust_lbls[:,0],:]

fig = plt.figure(1, figsize=(6, 4.5))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()
#labels = clst.labels_
#ax.scatter(coordF[:,0], coordF[:, 1], coordF[:, 2], s=200)
ax.scatter(coordClst[:,0], coordClst[:, 1], coordClst[:, 2], c=clust_lbls[:,1], s=200)
#plt.show()

#plt.plot(scr)
#plt.show()
