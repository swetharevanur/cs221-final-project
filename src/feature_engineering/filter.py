# filter.py
# Filters out all posts that dont have any
# of the important binary features
# Authors: Swetha Revanur and Keanu Spies

from feature_extractor import featureExtractor
import pandas as pd
import pickle

num_features = 19

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

column_order = ['postCategory', 'postDay','postDistrict','postID','postLocation','postMonth','postOtherAds','postPhone','postText','postTime','postTitle','postYear']

def exportDFtoExcel(df):
	df.to_excel('../../data/filtered_third_total_file_list.xlsx', index=False)

def exportJunktoExcel(df):
	df.to_excel('../../data/junk_third_total_file_list.xlsx', index=False)

def filterDF(df):
	junk = pd.DataFrame(columns = column_order)
	filtered = pd.DataFrame(columns = column_order)
	
	feature_vecs = {}
	junk_count = 0
	filter_count = 0
	for i in range(df.shape[0]):
		currentText = df.iat[i,8]
		if isFloat(df.iat[i,8]):
			feature_vecs[df.iat[i,3]] = [0]*num_features
			junk.loc[junk_count] = df.iloc[i]
			junk_count += 1
			continue

		feature_vec = featureExtractor(currentText)
		feature_vecs[df.iat[i,3]] = feature_vec
		score = sum(feature_vec)
		
		if score == 0:
			junk.loc[junk_count] = df.iloc[i]
			junk_count += 1
		else:
			filtered.loc[filter_count] = df.iloc[i]
			filter_count += 1

	with open("feature_vecs.pickle",'wb') as f:
		pickle.dump(feature_vecs,f)
	return filtered, junk

def importFilesAsDF():
	fileName = "../../data/third_total_file_list.xlsx"
	return pd.read_excel(fileName)

def main():
	totalDataFrame = pd.DataFrame()
	df = importFilesAsDF()
	filtered, junk = filterDF(df)
	exportDFtoExcel(filtered)
	exportJunktoExcel(junk)

main()