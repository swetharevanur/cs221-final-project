# backpage_parser.py
# HTML parser for a Backpages post (by URL)
# Retrieves post text, date, title, location, ID, and phone number.
# Authors: Swetha Revanur and Keanu Spies

import nltk
from nltk.tokenize.moses import MosesTokenizer
import urllib
from bs4 import BeautifulSoup
import re
import string
import pandas as pd
from util import stripPunctuation, stripAlpha, stripTags, stripPunctuationWithoutSpace, stripBreaks, stripUIB
import openpyxl # to create xlsl spreadsheet from pandas
import time
import copy
# from emoji_parse import replaceEmojis

def getPostText(soup, hasPostingBody):
	dataToReturn = []
	# if hasPostingBody:
	# 	tag = "postingBody"
	# else:
	# 	tag = "mainBody"

	for paragraph in soup.find("div", {"class" : "postingBody"}):
		p = unicode(paragraph)
		p = stripBreaks(p)
		p = stripUIB(p)
		# p = stripTags(p)
		dataToReturn.append(p)
	return ' '.join(dataToReturn)

def getPostDate(soup):
	result = ""
	for line in soup.find("div", {"class" : "adInfo"}):
		result += line.split("Posted:", 1)[1]
	result.split(' ')
	full_date = result.strip().split(' ')
	month = stripPunctuationWithoutSpace(full_date[1])
	day = stripPunctuationWithoutSpace(full_date[2])
	year = stripPunctuationWithoutSpace(full_date[3])
	time = stripPunctuationWithoutSpace(full_date[4])
	ampm = stripPunctuationWithoutSpace(full_date[5])
	if ampm == "PM":
		time = int(time) + 1200
	return month, day, year, time

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
		
def getPostPhoneNumber(tokenizedText):
	phoneNo = []
	pattern = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
	phoneNumbers = re.findall(pattern, tokenizedText) 
	if phoneNumbers is not None:
		for phoneNumber in phoneNumbers:
			phoneNumber = stripPunctuation(phoneNumber)
			phoneNumber = ''.join(phoneNumber.split(" "))
			if phoneNumber not in phoneNo:
				phoneNo.append(phoneNumber)
	return ' '.join(phoneNo)


def getOtherAdsByUser(soup):
	otherAds = []
	for line in soup.findAll("div", {"class" : "cat"}):
		for a in line.find_all('a', {"class" : "resultsSectionLabel"}, href = True):
			a.extract() # remove standard links
		for a in line.find_all('a', href = True):
			url = a['href'].split('/')
			postID = url[len(url) - 1]
			otherAds.append(postID)
	return otherAds

def getCategory(soup):
	cookieCrumb = soup.find("div", {"id" : "cookieCrumb"})
	categoryPath = cookieCrumb.findAll('a')
	for span in categoryPath[len(categoryPath) - 1].findAll('span'):
		span.extract()
	return categoryPath[len(categoryPath) - 1].text

def parsePost(url):
	information = urllib.urlopen(url).read()
	soup = BeautifulSoup(information, "html.parser")
	# remove line breaks
	for b in soup.findAll("br"):
		if "Post" in b.get_text().split():
			continue
		b.replace_with(" ")

	# map data 
	post = {}
	
	# page not found Error 535
	hasPostingBody = True
	if soup.find("div", {"class" : "postingBody"}) is None:
		# global errorCounter 
		# errorCounter += 1
		print "No postingBody found for: " + url
		return None
		# if soup.find("div", {"class" : "mainBody"}) is None: 
		# 	print url		
		# 	return None
		# hasPostingBody = False
	
	# populated map
	post['postText'] = getPostText(soup, hasPostingBody)
	post['postMonth'], post['postDay'], post['postYear'], post['postTime'] = getPostDate(soup)
	post["postTitle"] = getPostTitle(soup)
	post['postLocation'] = getPostLocation(soup)
	post['postDistrict'], post['postID'] = getPostDistrictID(soup)
	post['postPhone'] = getPostPhoneNumber(post['postText'])
	post['postOtherAds'] = getOtherAdsByUser(soup)
	post['postCategory'] = getCategory(soup)
	return post

def tabulate(URLS, batch):
	postData = []
	for URL in URLS:
		parseData = parsePost(URL)
		if parseData is not None:
			postData.append(parseData)

	url_df = pd.DataFrame(postData)
	filename = "../data/raw/thirdpostbatch" + str(batch) + ".xlsx"
	# print "URL PARSE FAILED " + errorCounter
	url_df.to_excel(filename, index=False, encoding ='unicode-escape') # for csv 

# tabulate(['http://losangeles.backpage.com/TherapeuticMassage/young-baba-massage-cute-and-hot-young-masseuses-great-fun-and-relaxation/146713767'], 9)
# tabulate(['http://losangeles.backpage.com/TherapeuticMassage/new-9-3-latina-girls-50-1hr-50-1hr-grand-opening/136704963',
# 'http://losangeles.backpage.com/TherapeuticMassage/asian-sexy-anywhere-out-to-you-new-face-fantastic-626-722-5855/119050048'], 90)
