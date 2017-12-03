# keyword_features.py
# checks for the presense of features such as 
# countries of interest, multiple victims and 
# victim weight

import re

countries_of_interest = ['china', 'vietnam', 'korea', 'thailand']
multiple_victims_keywords = ['girls', 'women', 'men', 'boys', 'people', 'children']
weight_boundary = 110

def containsCountriesOfInterest(text):	
	return 1 if any(country in text for country in countries_of_interest) else 0

def multipleVictimsAdvertised(text):
	return 1 if any(keyword in text for keyword in multiple_victims_keywords) else 0

def victimWeightMentioned(text):
	m = re.match(r'(?P<weight>\d+) (lbs)', text)
	return 1 if int(m.group('weight')) <= weight_boundary else 0

def containsWebsite(text):
	return 1 if 'http' in text else 0

