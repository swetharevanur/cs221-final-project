# kmeans_projection.py
# Creates 2D-projection using t-SNE transformation to visualize K-means clusters. 
# Authors: Swetha Revanur and Keanu Spies

import glob
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pickle as pkl
import copy

def importFeatureVecs():
	with open("../feature_engineering/feature_vecs.pickle",'r') as f:
		feature_vecs = pkl.load(f)
	df = pd.DataFrame.from_dict(feature_vecs)
	return df

df = importFeatureVecs()

# apply t-SNE projection
X = np.array([df[post] for post in df.columns])
X_embedded = TSNE(n_components=2).fit_transform(X) # convert to 2D (x, y) pair

# run k-means
kmeans = KMeans(n_clusters=2, random_state=0).fit(X_embedded)
y_kmeans = kmeans.predict(X_embedded)

# visualize
plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.xlim(-80, 80)
plt.ylim(-80, 80)
plt.show()




