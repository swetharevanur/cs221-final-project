# labeled_data.py
# Randomly generates subset of data (300 examples) to be manually labeled.
# Authors: Swetha Revanur and Keanu Spies

import pandas as pd
from random import randint
import numpy as np

def importFileAsDF():
	pathToFiles =r'../../data' # use your path
	fileName = pathToFiles + "/filtered_third_total_file_list.xlsx"
	
	df = pd.read_excel(fileName)
	return df

df = importFileAsDF()

num_records = len(df)
num_rand = 300
randRecordInds = []
for i in range(num_rand):
	while True:
		rand = randint(0, num_records)
		if rand not in randRecordInds:
			randRecordInds.append(rand)
			break

labeledDF = df.iloc[randRecordInds]

def diff(first, second):
	second = set(second)
	return [item for item in first if item not in second]
unlabeledInds = diff(range(0, num_records), randRecordInds)
unlabeledDF = df.iloc[unlabeledInds]

def exportDFtoExcel(totalDataFrame, path):
	totalDataFrame.to_excel(path, index=False)

exportDFtoExcel(labeledDF, '../../data/labeled_third_total_file_list.xlsx')
exportDFtoExcel(unlabeledDF, '../../data/unlabeled_third_total_file_list.xlsx')

