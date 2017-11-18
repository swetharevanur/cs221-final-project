# Authors: Swetha Revanur and Keanu Spies

import pandas as pd
import tensorflow as tf

filename = "../data/raw/postbatch7.xlsx"

# Step 1: Read the data into a list of strings.
def read_data(filename):
	# df = pd.read_excel(filename)
	# text = df['postText'].values # numpy.ndarray type
	# data = tf.compat.as_str("".join(text)).split()
	# return data
	data = "ebddtiayana elites vip athletes fun big booty fun rubs fetish 2egentleman and master his craft can do better than any fem 3pexotic thickness young freaky tight 2ohow many licks takes 2gtomorrow downtown blessing animals pet owners come join usflappers late night no blender bar show open mic wed sat 11 eopmsee craig shoemaker lovemaster live flapperscuban petes latin night club new years eve 2013 brazilian carnaval masquerade ballearth day festival bike ride city hall sat apr zoth lam ipmdowntown culver city third wednesday neighborhood step out spring happy hourdreamgirlsspoken funk not not not has not have not no joke showearthday 2013 inglewood city hall sat apr ieth iiam epmznd annual earth strong festival konshens richie spice warrior king dee lovaboyoperaworks presents arias motionhalloween event sea mountain nude lifestyle couples resort las vegas and palm springszouk masquerade ball 2013 zouk dallas monday 31 december 201zno tricks just treats gorgeous white girl fundeep tissue massage stress relief russian girl waiting you great relaxationmassage latina hottestsexy hot curvy latinas best townu r model availablesea salt and air heavenly massage upscale brunette please call advancebest place latinas 323973609zsexy young pretty asian massage new management 405 fwy exit artesia blvd torranceupscale redbone beauty young fun sweet slim and curvy sensationgrand opening grand opening grand opening 310 679 888bsexy asian bare 626297364psweet fiona petite asain torrance san pedro private incallandrea naughty girl next door private homenuru busty otties latina come babes call now 562 351 2765 we open lateholiday special best touch best time 702 502 874psweet taiwanese girl out your placegood massage shemale available now new new 657 201 075ohands experiencemassage special 80 562 528 490pmy last day new hot asian petitebest back babyhey let dim lights and soft music all you need and than some more 562 565 341lmature lovely petite and skilledhottest college aged latinas blue sky aroma pick your girl 562 968 988gpure bliss massage incall northridge independent tall native american euro mixloving sensual mature lady 4gbare asian hot 626342864enuru massage exotic dominican mixlet me your morning afternoon delight sweet brunette come youauthentic vixan latina highly well reviewedhottest world here isabelmature masseuse sailboat massagereal photos up early hot sexy and ready sheryl best rubdown sfv 2oohrblessed curves thighs thunder hips heavenme latina beauty 100 independent hotel home out call massageindian mix delight bubble ooty ioo realupscale redbone beauty young fun sweet slim and curvy sensationiippp 1992 nissan 3oozx import classic los angeles caaps forks classzi 999 stop call us more information our 2012 bmw series only 58 862 milesii 995 impressive 2016 toyota corolla only 32 875 mileszg 000 2010 toyota tundrapps look just came 2014 nissan maxima 82 239 mileszi 999 2013 bmw 3zbiig 495 impressive 2013 infiniti gel sedan only 49 463 mileszzooo 1958 ford fioo classic truck los angeles calpoo 2006 bmw 750 sedan marina del rey ca"
	return data.split()

vocabulary = read_data(filename)
print('Data size', len(vocabulary))

# Step 2: Build the dictionary and replace rare words with UNK token.
vocabulary_size = 50000

def build_dataset(words, n_words):
	"""Process raw inputs into a dataset."""
	count = [['UNK', -1]]
	count.extend(collections.Counter(words).most_common(n_words - 1))
	dictionary = dict()
	for word, _ in count:
		dictionary[word] = len(dictionary)
	data = list()
	unk_count = 0
	for word in words:
		index = dictionary.get(word, 0)
	if index == 0:  # dictionary['UNK']
		unk_count += 1
	data.append(index)
	count[0][1] = unk_count
	reversed_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
	return data, count, dictionary, reversed_dictionary

# Filling 4 global variables:
# data - list of codes (integers from 0 to vocabulary_size-1).
#   This is the original text but words are replaced by their codes
# count - map of words(strings) to count of occurrences
# dictionary - map of words(strings) to their codes(integers)
# reverse_dictionary - maps codes(integers) to words(strings)
data, count, dictionary, reverse_dictionary = build_dataset(vocabulary,vocabulary_size)
del vocabulary  # to reduce memory.
print('Most common words (+UNK)', count[:5])
print('Sample data', data[:10], [reverse_dictionary[i] for i in data[:10]])

data_index = 0


