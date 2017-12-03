# label_spreading.py
# Semi-supervised label spreading with affinity matrix based \
# on the normalized graph Laplacian and soft clamping across the labels.
# Con: high memory consumption
# Authors: Swetha Revanur and Keanu Spies

import numpy as np
from sklearn import datasets
from sklearn.semi_supervised import LabelSpreading
label_prop_model = LabelSpreading(kernel='rbf', \
	gamma=20, n_neighbors=7, \
	alpha=0.2, max_iter=30, tol=1e-3, n_jobs=1)

iris = datasets.load_iris()

rng = np.random.RandomState(42)
random_unlabeled_points = rng.rand(len(iris.target)) < 0.3
labels = np.copy(iris.target)

labels[random_unlabeled_points] = -1
label_prop_model.fit(iris.data, labels)

# label_prop_model.predict()
# label_prop_model.score()
