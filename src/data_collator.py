# data_collator.py

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

	totalDataFrame.to_excel('total_file_list.xlsx', index=False)

# def writeToExcel:

# global total_df
# total_df = pd.DataFrame()

# def importFilesAsDF:
# 	for i in range(1,65):
# 		filename = 'data' + str(i) + '.xslx'
# 		this_df = pd.read_excel(filename)



importFilesAsDF()