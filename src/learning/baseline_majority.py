# baseline_majority.py
# Runs our baseline on our labeled set
# and performs analysis on the results
import pandas as pd
import numpy as np
from sklearn.metrics import precision_recall_fscore_support
INDEX_OF_LABEL = 12

def importFileAsDF(filename):
	pathToFiles = './' # use your path
	fileNames = pathToFiles + filename
	df = pd.read_excel(fileNames)
	return df

def loadDataSet(df):
	return df.values.tolist()

def getMajority(data_list):
	ones_count = 0
	zeros_count = 0
	for i in range(int(0.8*len(data_list))):
		label = data_list[i][INDEX_OF_LABEL]
		if label == 1: ones_count += 1
		else: zeros_count += 1

	majority = -1
	if ones_count > zeros_count: majority = 1
	else: majority = 0

	true_data_vec = []
	for i in range(int(0.8*len(data_list)), int(len(data_list))):
		label = data_list[i][INDEX_OF_LABEL]
		true_data_vec.append(label)

	return majority, true_data_vec

def __init__():
	df = importFileAsDF('../../data/labeled_third_total_file_list.xlsx')
	data_list = loadDataSet(df)
	majority, true_data_vec = getMajority(data_list)
	y_pred = [majority]*len(true_data_vec)
	ones_count = sum(true_data_vec)
	total = len(true_data_vec)
	true_data_vec = np.array(true_data_vec)
	y_pred = np.array(y_pred)

	tp = ones_count
	fp = total - ones_count
	tn = 0
	fn = 0
	accuracy1 = float(tp + tn)/(tp + tn + fp + fn)

	tp = 0
	fp = 0
	tn = ones_count
	fn = total - ones_count
	accuracy2 = float(tp + tn)/(tp + tn + fp + fn)

	total_accuracy = (accuracy1+accuracy2)/2
	print total_accuracy

__init__()