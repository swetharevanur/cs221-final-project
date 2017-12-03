# lda.py
# LDA topic-modeling to derive secondary feature vector
# Authors: Swetha Revanur and Keanu Spies

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import pandas as pd
import glob
import math

tokenizer = RegexpTokenizer(r'\w+')
	
# create sample documents
doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health." 

def importFilesAsDF():
	pathToFiles =r'../../data' # use your path
	fileNames = glob.glob(pathToFiles + "/second_total_file_working*.xlsx")
	
	postList = []
	for fileName in fileNames:
		df = pd.read_excel(fileName)
		postList.append(df)

	totalDataFrame = pd.concat(postList)
	return totalDataFrame

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
	if isFloat(text): text = ""
	if isFloat(title): title = ""
	currentText = text + title
	doc_set.append(currentText)

# compile sample documents into a list
# doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
	# clean and tokenize document string
	raw = i.lower()
	tokens = tokenizer.tokenize(raw)
	# add tokens to list
	texts.append(tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
	
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
# optimal number of topics computed in lda_tuning.R
opt_num_topics = 5
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=opt_num_topics, id2word = dictionary, passes=20, minimum_probability=0.0)

# print ldamodel.print_topics(num_topics=25, num_words=4)
print ldamodel.print_topics(num_topics=5, num_words=4)
for i in range(10):
	print ldamodel[corpus[i]]
