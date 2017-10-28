# backpage_parser.py
# HTML parser for a Backpages post (by URL)
# Retrieves post text, date, title, location, ID, and phone number.
# Author: Swetha Revanur

import nltk
import urllib
from bs4 import BeautifulSoup
import re
import string
from util import stripPunctuation

def getPostText(soup):
	dataToReturn = []
	for paragraphs in soup.find("div", {"class" : "postingBody"}):
		sentences = nltk.word_tokenize(paragraphs)
		if len(sentences) == 0:
			continue
		for word in sentences:
			dataToReturn.append(word)
	return dataToReturn


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
	for word in tokenizedText:
		if re.match(pattern, word) is not None:
			word = stripPunctuation(word)
			if word not in phoneNo:
				phoneNo.append(word)
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
 

# doesn't handle non-unicode emoji characters
def parsePost(url):
	information = urllib.urlopen(url).read()
	soup = BeautifulSoup(information)
	# remove line breaks
	for b in soup.findAll("br"):
		b.extract()

	postText = getPostText(soup)
	print postText

	postMonth, postDay, postYear, postTime = getPostDate(soup)
	print postMonth, postDay, postYear, postTime

	postTitle = getPostTitle(soup)
	print postTitle

	postLocation = getPostLocation(soup)
	print postLocation

	postDistrict, postID = getPostDistrictID(soup)
	print postID

	postPhone = getPostPhoneNumber(postText)
	print postPhone

	postOtherAds = getOtherAdsByUser(soup)
	print postOtherAds

URLs = ["http://losangeles.backpage.com/AppliancesForSale/over-15-years-refrigerator-fixer-24-hrs-emergency-store-3106972751-same-day-nights-also/99071977",
		"http://losangeles.backpage.com/TherapeuticMassage/south-american-therapist-to-your-door/92268987",
		"http://losangeles.backpage.com/TherapeuticMassage/40-intoxicating-colombian-and-asian-chicks-will-oil-you-til-your-toes-curl-310-849-4388/121253938",
		"http://losangeles.backpage.com/ElectronicsForSale/1-199-13-macbook-air-core-i7-2-2-8gb-ram-500ssd-latest-models/145134832",
		"http://sf.backpage.com/TherapeuticMassage/and-call-me-today-650-246-0113-hot-sweet-asian-girl-outcall-only-and/48972132",
		"http://losangeles.backpage.com/TherapeuticMassage/six-cute-asians-everyday-largest-spa-in-pasadena-seven-massage-rooms-open-late/143424287"]

parsePost(URL)
