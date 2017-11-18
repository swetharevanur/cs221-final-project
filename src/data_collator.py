# data_collator.py
# Given our set of excel files produced in the webcrawler
# collates date into one excel file
# Authors: Swetha Revanur and Keanu Spies

import pandas as pd
import glob
import openpyxl
import xlrd
from preprocessing import preprocess

def importFilesAsDF(totalDataFrame):
	pathToFIles =r'../data' # use your path
	fileNames = glob.glob(pathToFIles + "/postbatch*.xlsx")
	
	listOfData = []
	for fileName in fileNames:
	    df = pd.read_excel(fileName)
	    listOfData.append(df)
	
	totalDataFrame = pd.concat(listOfData)
	return totalDataFrame

def preprocessDF(totalDataFrame):
	for i in range(totalDataFrame.shape[0]):
		currentText = totalDataFrame.iat[i,8]
		preprocessedText = preprocess(currentText)
		totalDataFrame.set_value(i, 'postText', preprocessedText)
		currentTitle = totalDataFrame.iat[i,10]
		preprocessedTitle = preprocess(currentTitle)
		totalDataFrame.set_value(i, 'postTitle', preprocessedTitle)

def exportDFtoExcel(totalDataFrame):
	totalDataFrame.to_excel('../data/total_file_list.xlsx', index=False)

def __init__():
	totalDataFrame = pd.DataFrame()
	totalDataFrame = importFilesAsDF(totalDataFrame)
	preprocessDF(totalDataFrame)
	exportDFtoExcel(totalDataFrame)

__init__()
