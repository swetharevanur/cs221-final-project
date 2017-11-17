# data_collator.py
# Given our set of excel files produced in the webcrawler
# collates date into one excel file
# Authors: Swetha Revanur and Keanu Spies

import pandas as pd
import glob
import openpyxl
import xlrd

def importFilesAsDF():
	pathToFIles =r'../data' # use your path
	fileNames = glob.glob(pathToFIles + "/postbatch*.xlsx")
	totalDataFrame = pd.DataFrame()
	listOfData = []
	for fileName in fileNames:
	    df = pd.read_excel(fileName,index_col=None)
	    listOfData.append(df)
	totalDataFrame = pd.concat(listOfData)

	totalDataFrame.to_excel('../data/total_file_list.xlsx', index=False)

importFilesAsDF()