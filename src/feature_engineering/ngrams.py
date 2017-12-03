from nltk import ngrams

def tf_idf(text):
	ngrams_set = ngrams(text.split(), 3)
	for ngram in ngrams_set:
		