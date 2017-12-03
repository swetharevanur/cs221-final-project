# read_data.py
# Imports filtered, preprocessed data as data structure
# Authors: Swetha Revanur and Keanu Spies

import os
import urllib
import pandas as pd

def importFilesAsDF(totalDataFrame):
	pathToFiles =r'../data/raw' # use your path
	fileNames = glob.glob(pathToFiles + "/secondpostbatch*.xlsx")
	
	postList = []
	for fileName in fileNames:
		df = pd.read_excel(fileName)
		postList.append(df)
	
	totalDataFrame = pd.concat(postList)
	return totalDataFrame
