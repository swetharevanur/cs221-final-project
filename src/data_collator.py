# data_collator.py
# Given our set of excel files produced in the webcrawler
# collates date into one excel file
# Authors: Swetha Revanur and Keanu Spies

import pandas as pd
import glob
import openpyxl
import xlrd
from preprocessing import preprocess
import math

def importFilesAsDF(totalDataFrame):
	pathToFiles =r'../data/raw' # use your path
	fileNames = glob.glob(pathToFiles + "/postbatch*.xlsx")
	
	listOfData = []
	for fileName in fileNames:
	    df = pd.read_excel(fileName)
	    listOfData.append(df)
	
	totalDataFrame = pd.concat(listOfData)
	return totalDataFrame

def preprocessDF(totalDataFrame):
	fullfile = ''
	for i in range(totalDataFrame.shape[0]):
	# for i in range(160,162):
		currentText = totalDataFrame.iat[i,8]
		preprocessedText = preprocess(currentText)		
		fullfile += ' ' + preprocessedText
		totalDataFrame.iloc[i, totalDataFrame.columns.get_loc('postText')] = preprocessedText
		
		currentTitle = totalDataFrame.iat[i,10]
		if isinstance(currentTitle, float): continue
		preprocessedTitle = preprocess(currentTitle)
		totalDataFrame.iloc[i, totalDataFrame.columns.get_loc('postTitle')] = preprocessedTitle
	return fullfile

def exportDFtoExcel(totalDataFrame):
	totalDataFrame.to_excel('../data/total_file_list.xlsx', index=False)
	
def __init__():
	totalDataFrame = pd.DataFrame()
	totalDataFrame = importFilesAsDF(totalDataFrame)
	fullfile = preprocessDF(totalDataFrame)
	exportDFtoExcel(totalDataFrame)

__init__()
