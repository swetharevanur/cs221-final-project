# label_spreading.py
# Semi-supervised label spreading with affinity matrix based \
# on the normalized graph Laplacian and soft clamping across the labels.
# Con: high memory consumption
# Authors: Swetha Revanur and Keanu Spies

# import numpy as np
# from sklearn import datasets
# from sklearn.semi_supervised import LabelSpreading
# label_prop_model = LabelSpreading(kernel='rbf', \
# 	gamma=20, n_neighbors=7, \
# 	alpha=0.2, max_iter=30, tol=1e-3, n_jobs=1)

# iris = datasets.load_iris()

# rng = np.random.RandomState(42)
# random_unlabeled_points = rng.rand(len(iris.target)) < 0.3
# labels = np.copy(iris.target)

# labels[random_unlabeled_points] = -1
# label_prop_model.fit(iris.data, labels)

# label_prop_model.predict()
# label_prop_model.score()

from sklearn import datasets
from sklearn.semi_supervised import LabelSpreading
import numpy as np
from scipy.sparse import csgraph
from openpyxl import load_workbook
import pandas as pd

def importFileAsDF(filename):
	pathToFiles = './' # use your path
	fileNames = pathToFiles + filename
	df = pd.read_excel(fileNames)
	return df

def labelSpread(df):
	label_prop_model = LabelSpreading()

	# unlabeled set 
	iris = datasets.load_iris()
	print iris.data
	rng = np.random.RandomState(42)
	random_unlabeled_points = rng.rand(len(iris.target)) < 0.3

	# labeled set	
	labels = np.copy(iris.target)
	labels[random_unlabeled_points] = -1
	label_prop_model.fit(iris.data, labels)

	y = label_prop_model.predict(iris.data)
	label_prop_model.score(iris.data, y)

def __init__():
	unlabeled_df = importFileAsDF("dummy_lda_output.xlsx")
	x = createDataSet(unlabeled_df)
	# labeled_df = importFileAsDF("dummy_labeled_lda_output.xlsx")
	labelSpread(unlabeled_df)

__init__()

