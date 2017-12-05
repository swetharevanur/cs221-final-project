# label_spreading.py
# Semi-supervised label spreading with affinity matrix based \
# on the normalized graph Laplacian and soft clamping across the labels.
# Con: high memory consumption
# Authors: Swetha Revanur and Keanu Spies

# import numpy as np
# from sklearn import datasets
# from sklearn.semi_supervised import LabelSpreading
# label_prop_model = LabelSpreading(kernel='rbf', \
#   gamma=20, n_neighbors=7, \
#   alpha=0.2, max_iter=30, tol=1e-3, n_jobs=1)

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
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import confusion_matrix, classification_report
import itertools

INDEX_OF_POSTID = 3

def importFileAsDF(filename):
	pathToFiles = './' # use your path
	fileNames = pathToFiles + filename
	df = pd.read_excel(fileNames)
	return df

def loadDataSet(df):
	return df.values.tolist()

def getXLabelVector(data_list, labeled_df):
	# labeled_list = labeled_df.values.tolist()
	# num_labels = 0

	# label_vector = []
	# labeled_X = []
	# unlabeled_data = []

	# for i in range(len(data_list)):
	#   labeled = False
	#   for label in labeled_list:
	#       if data_list[i][0] in label[0]:
	#           labeled = True
	#           label_vector.append(label[1])
	#           labeled_X.append(data_list[i][1:])
	#           num_labels += 1
	#           continue
	#   if not labeled:
	#       unlabeled_data.append(data_list[i])

	# return labeled_X, label_vector, unlabeled_data

	labeled_list = labeled_df.values.tolist()

	label_vector = []
	labeled_X = []
	unlabeled_X = []
	unlabeled_vec = []
	final_x = []

	for i in range(len(data_list)):
		labeled = False
		for label in labeled_list:
			if int(data_list[i][0]) == label[INDEX_OF_POSTID]:
				labeled = True
				label_vector.append(label[12])
				labeled_X.append(data_list[i][1:])
				break
		# if not labeled:
			# unlabeled_X.append(data_list[i][1:])
			# final_x.append(data_list[i])
			# unlabeled_vec.append(-1)

	labeled_X.extend(unlabeled_X)
	X = labeled_X
	label_vector.extend(unlabeled_vec)
	y = label_vector

	return X, y, final_x
	


# def getXLabelVector(data_list, labeled_df):
#   labeled_list = labeled_df.values.tolist()
#   label_vector = []
#   X = []
#   for i in range(len(data_list)):
#       for label in labeled_list:
#           if data_list[i][0] in label[0]:
#               label_vector.append(label[1])
#               X.append(data_list[i][1:])
#               break

#   return X,label_vector

def predictRestOfData(lp_model, data):
	X = [data_index[1:] for data_index in data]
	y = lp_model.predict(X)
	predictions = []
	for i in range(len(data)):
		prediction = {}
		prediction['postID'] = data[i][0]
		prediction['prediction'] = y[i]
		predictions.append(prediction)

	predict_df = pd.DataFrame(predictions)
	filename = 'predicted_labels.xlsx'
	predict_df.to_excel(filename, index=False)


def labelSpread(df,labeled_df):
	# load data and labels 
	data = loadDataSet(df)
	X,y,unlabeled_X= getXLabelVector(data,labeled_df)
	# rng = np.random.RandomState(0)
	indices = np.arange(len(X))
	# rng.shuffle(indices)

	n_total_samples = len(y)
	n_labeled_points = 130
	indices = np.arange(n_total_samples)
	unlabeled_set = indices[n_labeled_points:]
	y = np.array(y)

	# Shuffle everything around
	y_train = np.copy(y)
	y_train[unlabeled_set] = -1

	# lp_model = LabelSpreading(gamma=0.25, max_iter=500)
	lp_model = LabelSpreading(kernel = 'knn', n_neighbors = 13 ,max_iter=10000)
	lp_model.fit(X, y_train)
	predicted_labels = lp_model.transduction_[unlabeled_set]
	# saveToFile(predicted_labels, )
	true_labels = y[unlabeled_set]

	cm = confusion_matrix(true_labels, predicted_labels, labels=lp_model.classes_)

	print("Label Spreading model: %d labeled & %d unlabeled points (%d total)" %
	  (n_labeled_points, n_total_samples - n_labeled_points, n_total_samples))
	print(classification_report(true_labels, predicted_labels))
	print("Confusion matrix")
	print(cm)
	# predictRestOfData(lp_model, unlabeled_X)
	classes = ['0', '1']

	cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
	plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Reds)
	plt.title('Normalized confusion matrix')
	plt.colorbar()
	tick_marks = np.arange(len(classes))
	plt.xticks(tick_marks, classes, rotation=45)
	plt.yticks(tick_marks, classes)

	fmt = '.2f' if True else 'd'
	thresh = cm.max() / 2.
	for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
		plt.text(j, i, format(cm[i, j], fmt),
				 horizontalalignment="center",
				 color="white" if cm[i, j] > thresh else "black")

	plt.tight_layout()
	plt.ylabel('True label')
	plt.xlabel('Predicted label')
	plt.show()


def __init__():
	lda_df = importFileAsDF("../../../data/lda_features.xlsx")
	# labeled_df = importFileAsDF("../../../data/labeled_third_total_file_list.xlsx")
	labeled_df = importFileAsDF("../../../data/labeled_third_total_file_list.xlsx")
	labelSpread(lda_df, labeled_df)

__init__()

