# -*- encoding: utf8 -*-
# lda.py
# LDA topic-modeling to derive secondary feature vector
# Authors: Swetha Revanur and Keanu Spies

from gensim import corpora, models
import gensim
import pandas as pd
import math

def importFilesAsDF():
	pathToFiles =r'../../data' # use your path
	fileName = pathToFiles + "/filtered_third_total_file_list.xlsx"
	
	df = pd.read_excel(fileName)
	return df

df = importFilesAsDF()

doc_set = []

def isFloat(string):
	try:
		float(string)
		return True
	except ValueError:
		return False

for i, row in df.iterrows():
	text = df.iat[i,8]
	title = df.iat[i,10]
	# text is nan if cell is empty, so just catch and change to empty string
	if isFloat(text): text = ""
	if isFloat(title): title = ""
	currentText = text + title
	doc_set.append(currentText)

texts = []
# loop through document list
for doc in doc_set:
	texts.append(doc.split())

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
	
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
# optimal number of topics computed in lda_tuning.R
opt_num_topics = 3
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=opt_num_topics, id2word = dictionary, passes=20, minimum_probability=0.0)

# print ldamodel.print_topics(num_topics=opt_num_topics, num_words=4)

# create feature vector dataframe
# posts are rows and cols are vector components
index = df['postID']
columns = ['phi_' + str(i) for i in range(opt_num_topics)]

# featureDF = featureDF.fillna(0)

rows = []
for i in range(1857):
	vals = {'phi_' + str(x): y for x,y in ldamodel[corpus[i]]}
	rows.append(vals)
	# print vals
	# featureDF.iloc[[i]] = vals

featureDF = pd.DataFrame(rows, index=index, columns=columns)

def exportDFtoExcel(totalDataFrame):
	totalDataFrame.to_excel('../../data/lda_features.xlsx', index=True)

exportDFtoExcel(featureDF)
	


