# -*- encoding: utf-8-*-

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
from util import stripPunctuation, stripAlpha, stripTags
import openpyxl # to create xlsl spreadsheet from pandas
import time
from emoji_parse import replaceEmojis

def getPostText(soup):
	dataToReturn = []
	for paragraph in soup.find("div", {"class" : "postingBody"}):
		# replace emojis in text with key-words
		# paragraph = replaceEmojis(paragraph)
		# remove excess newline chars
		paragraph = str(paragraph).strip()
		# remove tags such as <b>	
		paragraph = stripTags(str(paragraph))
		dataToReturn.append(paragraph)
	return ' '.join(dataToReturn)


def getPostDate(soup):
	result = ""
	for line in soup.find("div", {"class" : "adInfo"}):
		result += line.split("Posted:", 1)[1]
	result.split(' ')
	full_date = result.strip().split(' ')
	month = stripPunctuation(full_date[1])
	day = stripPunctuation(full_date[2])
	year = stripPunctuation(full_date[3])
	time = stripPunctuation(full_date[4])
	ampm = stripPunctuation(full_date[5])
	if ampm == "PM":
		time = int(time) + 1200
	return month, day, year, time


def getPostTitle(soup):
	result = ""
	for line in soup.find("a", {"class" : "h1link"}):
		result += line.get_text()
	# result = replaceEmojis(result)
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
	if soup.find("div", {"class" : "postingBody"}) is None: 
		print url		
		return None
	# populated map
	post['postText'] = getPostText(soup)
	# print post['postText']	
	post['postMonth'], post['postDay'], post['postYear'], post['postTime'] = getPostDate(soup)
	post["postTitle"] = getPostTitle(soup)
	post['postLocation'] = getPostLocation(soup)
	post['postDistrict'], post['postID'] = getPostDistrictID(soup)
	post['postPhone'] = getPostPhoneNumber(post['postText'])
	# print post['postPhone']
	post['postOtherAds'] = getOtherAdsByUser(soup)
	return post

def tabulate(URLS):
	postData = []
	for URL in URLS: 
		parseData = parsePost(URL)
		if parseData is not None:
			postData.append(parseData)
	a = pd.DataFrame(postData)
	a.to_excel("data.xlsx") # for excel spreadsheet
	# a.to_csv("data.csv") # for csv 

tabulate(['http://losangeles.backpage.com/TherapeuticMassage/blissful-goddess-with-loving-hands/122215198'])
