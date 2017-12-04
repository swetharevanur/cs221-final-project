# keyword_features.py
# checks for the presense of features such as 
# countries of interest, multiple victims and 
# victim weight

import re

countries_of_interest = ['china', 'vietnam', 'korea', 'thailand', 'asian'] #TODO: add emojis of country flags
multiple_victims_keywords = ['girls', 'women', 'men', 'boys', 'people', 'children', 'babes', 'dolls', 'masseuses']
weight_boundary = 110
word_phrases = ['young', 'fresh', 'new', 'new in town', 'new arrrival', 'open minded', 'petite', \
'exotic', 'youthful', 'barely legal', 'virgin', 'tiny', 'incall','in call', 'new to the game', 'candy', ]

spa_and_massage = ['spa', 'massage']


def containsCountriesOfInterest(text):	
	return 1 if any(country in text for country in countries_of_interest) else 0

def multipleVictimsAdvertised(text):
	return 1 if any(keyword in text for keyword in multiple_victims_keywords) else 0

def victimWeightMentioned(text):
	m = re.search(r'(?P<weight>\d+)\s*(lb)', text)
	if not m: 
		return 0
	return 1 if int(m.group('weight')) <= weight_boundary else 0

def presenceOfPhrasesAndWords(text):
	return 1 if any(word in text for word in word_phrases) else 0

def presenceOfSpa(text):
	return 1 if any(word in text for word in spa_and_massage) else 0

# def containsWebsite(text):
# 	return 1 if 'http' in text else 0

# print presenceOfPhrasesAndWords('in calp')