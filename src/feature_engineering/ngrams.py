# -*- encoding: utf8 -*-
# ngrams.py
# Given a doctument, performs tf_idf on the ngrams
# of that document and populates the tf-idf
# Authors: Swetha Revanur and Keanu Spies

from nltk import ngrams
from corpus_idf import createCorpus
from collections import defaultdict
import pandas as pd
import pickle
import operator

def computeTFMap(text):
	total_count = 0
	ngram_count = defaultdict(int)
	ngrams_set = ngrams(text.split(), 2)
	for ngram in list(ngrams_set):
		ngram_count[ngram] += 1
		total_count += 1
	tf_map = {}
	for ngram, count in ngram_count.iteritems():
		tf_map[ngram] = float(count)/total_count
	return tf_map

def readInIDFMap():
	idf = {}
	with open("idf_dict.pickle",'r') as f:
		idf = pickle.load(f)
	return idf

def tf_idf(text):
	tf_map = computeTFMap(text)
	# this needs to be preprocessed out
	idf_map = readInIDFMap()
	tf_idf = {}
	ngrams_set = ngrams(text.split(), 2)
	for ngram in list(ngrams_set):
		if ngram in idf_map: tf_idf[ngram] = 1
	for ngram in idf_map:
		if ngram not in tf_idf:
			tf_idf[ngram] = 0
	tf_list = []
	for ngram in dict(sorted(tf_idf.iteritems(), key=operator.itemgetter(1), reverse=True)):
		tf_list.append(tf_idf[ngram])
	return tf_list
# df = pd.read_excel('../../data/raw/postbatch1.xlsx')
# document = createCorpus(df)
# print tf_idf(document)