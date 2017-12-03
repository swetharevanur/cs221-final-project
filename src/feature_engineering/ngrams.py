# ngrams.py
# Given a doctument, performs tf_idf on the ngrams
# of that document and populates the tf-idf
# Authors: Swetha Revanur and Keanu Spies

from nltk import ngrams
from corlpus_idf import computeIDFMap

def computeTFMap(text):
	total_count = 0
	ngram_count = defaultdict(int)
	ngrams_set = ngrams(text.split(), 3)
	for ngram in list(ngrams_set):
		ngram_count[ngram] += 1
		total_count += 1
	tf_map = {}
	for ngram, count in ngram_count.iteritems():
		tf_map[ngram] = float(count)/total_count
	return tf_map

def tf_idf(text):
	tf_map = computeTFMap(text)
	# this needs to be preprocessed out
	idf_map = computeIDFMap('../../data/total_file_list.xlsx')
	tf_idf = {}
	ngrams_set = ngrams(text.split(), 3)
	for ngram in list(ngrams_set):
		tf_idf[ngram] = idf_map[ngram]*tf_map[ngram]
	return tf_idf