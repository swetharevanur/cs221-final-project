# -*- encoding: utf8 -*-
# corpus_idf.py
# performs idf on the corpus
# Authors: Swetha Revanur and Keanu Spies

from nltk import ngrams
from collections import defaultdict
from math import log
import pandas as pd
import re
import operator
import pickle

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def createCorpus(df):
	corpus = ''
	for i in range(df.shape[0]):
		if isFloat(df.iat[i,8]):
			continue
		corpus += df.iat[i,8]
	corpus = re.sub(r'\s+', ' ', corpus)
	return corpus

def calculateIDFMap(text):
	total_count = 0
	ngram_count = defaultdict(int)
	ngrams_set = ngrams(text.split(), 2)
	for ngram in list(ngrams_set):
		ngram_count[ngram] += 1
		total_count += 1
	idf_map = {}
	for ngram, count in ngram_count.iteritems():
		idf_map[ngram] = log(1 + float(count)/total_count)
	return idf_map

def computeIDFMap(filename):
	df = pd.read_excel(filename)
	corpus = createCorpus(df)
	idf_map = calculateIDFMap(corpus)
	n = 9
	top_n_vals = dict(sorted(idf_map.iteritems(), key=operator.itemgetter(1), reverse=True)[:n])
	# print sorted(top_n_vals.iteritems(),key=operator.itemgetter(1), reverse=True)
	with open("idf_dict.pickle",'wb') as f:
		pickle.dump(top_n_vals,f)

computeIDFMap('../../data/third_total_file_list.xlsx')
