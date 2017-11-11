# web_crawler.py
# Web crawler that recursively searches the entire Backpage website
# Retrieves post text, date, title, location, ID, and phone number.
# Authors: Swetha Revanur and Keanu Spies

import nltk
import urllib
from bs4 import BeautifulSoup
import re
import string
from util import stripPunctuation
from backpage_parser import * 

def getPostsOnPage(soup):
	urls = []
	pattern = '\S*/\d{9}'	
	for a in soup.findAll('a', attrs={'href': re.compile("^http://")}):
		url = a['href']
		if re.match(pattern, url) is not None:
			if url not in urls:
				urls.append(url)
	return urls

def getPagesFromRegion(soup, region):
	urls = []
	for a in soup.findAll('a', attrs={'href': re.compile("^http://")}):
		url = a['href']
		if "Disclaimer" in url:			
			if url not in urls:
				url = url[:url.rfind("?")]
				url = re.sub("classifieds/Disclaimer", "", url)
				urls.append(url)
	return urls

def getDataFromPagesInRegion():
	region = "http://losangeles.backpage.com/"
	information = urllib.urlopen(region).read()
	soup = BeautifulSoup(information, "html.parser")
	pages = getPagesFromRegion(soup, region)
	URLS = []
	for page in pages:
		page_information = urllib.urlopen(page).read()
		page_soup = BeautifulSoup(page_information, "html.parser")
		URLS.extend(getPostsOnPage(page_soup))
	tabulate(URLS)

getDataFromPagesInRegion()

