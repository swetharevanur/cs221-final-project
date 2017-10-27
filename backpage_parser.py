# backpage_parser.py
# HTML parser for a Backpages post (by URL)
# Retrieves post text, date, title, location, ID, and phone number.
# Author: Swetha Revanur

import nltk
import urllib
import requests
from bs4 import BeautifulSoup

def getPostText(soup):
	dataToReturn = []
	for paragraphs in soup.find("div", {"class" : "postingBody"}):
		sentences = nltk.word_tokenize(paragraphs)
		if len(sentences) == 0:
			continue
		# print sentences
		for word in sentences:
			dataToReturn.append(word)
	return dataToReturn


def getPostDate(soup):
	result = ""
	for line in soup.find("div", {"class" : "adInfo"}):
		result += line.split("Posted:", 1)[1]
	return result.strip()


def getPostTitle(soup):
	result = ""
	for line in soup.find("a", {"class" : "h1link"}):
		result += line.get_text()
	return result.strip()


def getPostLocation(soup):
	result = ""
	for line in soup.findAll("div", style = "padding-left:2em;"):
		line = line.get_text().strip()
		if "Location:" not in line:
			continue
		result += line.split("Location:", 1)[1]
	return result.strip()


def getPostDistrictID(soup):
	result = ""
	for line in soup.findAll("div", style = "padding-left:2em;"):
		line = line.get_text().strip()
		if "Post ID:" not in line:
			continue
		result += line.split("Post ID:", 1)[1]
	return [result.split()[1].strip(), result.split()[0].strip()]
		

# doesn't handle non-unicode emoji characters
def parsePost(url):
	information = urllib.urlopen(url).read()
	soup = BeautifulSoup(information)
	# remove line breaks
	for b in soup.findAll("br"):
		b.extract()

	postText = getPostText(soup)
	print postText
	postDate = getPostDate(soup)
	print postDate
	postTitle = getPostTitle(soup)
	print postTitle
	postLocation = getPostLocation(soup)
	print postLocation
	postDistrict, postID = getPostDistrictID(soup)
	print postDistrict, postID

	
URL = 'http://losangeles.backpage.com/AppliancesForSale/over-15-years-refrigerator-fixer-24-hrs-emergency-store-3106972751-same-day-nights-also/99071977'
parsePost(URL)
