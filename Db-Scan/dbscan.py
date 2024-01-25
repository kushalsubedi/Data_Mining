import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import DBSCAN 
from sklearn import metrics 
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs
# Generate sample data 

X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4, random_state=0)

# Normalize dataset for easier parameter selection
X = StandardScaler().fit_transform(X)

# Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True 

labels = db.labels_ 

# Number of clusters in labels, ignoring noise if present 
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0) 

# Black removed and is used for noise instead. 
unique_labels = set(labels) 
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels))) 

# Plot the points with colors
for k, col in zip(unique_labels, colors): 
    if k == -1: 
        # Black used for noise. 
        col = 'k' 

    class_member_mask = (labels == k) 

    xy = X[class_member_mask & core_samples_mask] 
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14) 

#plot the border points 
    xy = X[class_member_mask & ~core_samples_mask] 
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=6) 

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()



