# filter.py
# Filters out all posts that dont have any
# of the important binary features
# Authors: Swetha Revanur and Keanu Spies

from feature_extractor import featureExtractor
import pandas as pd
import pickle

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def exportDFtoExcel(df):
	df.to_excel('../../data/filtered_third_total_file_list.xlsx', index=False)

def filterDF(df):
	filtered = pd.DataFrame()
	feature_vecs = {}
	for i in range(df.shape[0]):
		currentText = df.iat[i,8]
		if isFloat(df.iat[i,8]):
			continue
		feature_vec = featureExtractor(currentText)
		feature_vecs[df.iat[i,3]] = feature_vec
		score = sum(feature_vec)
		if score == 0: 
			df.drop(i)
	with open("feature_vecs.pickle",'wb') as f:
			pickle.dump(feature_vecs,f)	
	return df

def importFilesAsDF():
	fileName = "../../data/third_total_file_list.xlsx"
	return pd.read_excel(fileName)

def main():
	totalDataFrame = pd.DataFrame()
	df = importFilesAsDF()
	df = filterDF(df)
	exportDFtoExcel(df)

main()