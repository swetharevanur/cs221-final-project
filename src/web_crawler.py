# web_crawler.py
# Web crawler that recursively searches the entire Backpage website
# Retrieves post text, date, title, location, ID, and phone number.
# Authors: Swetha Revanur and Keanu Spies

import nltk
import urllib
from bs4 import BeautifulSoup
import re
import string
import pandas as pd
from util import stripPunctuation
from backpage_parser import * 

def getPostsOnPage(soup):
	urls = set()
	patternShort = '\S*/\d{8}'	
	patternLong = '\S*/\d{9}'	
	for a in soup.findAll('a', attrs={'href': re.compile("^http://")}):
		url = a['href']
		if re.match(patternShort, url) is not None or re.match(patternLong, url) is not None:
			urls.add(url)
	return urls

def getPagesFromRegion(soup, region):
	urls = set()
	sampleCategories = ["/MusicianWanted/", "/events/", "/real-estate-wanted/", "/AccountingJobs/", \
		"/Childcare/", "/Farm/", "/FurnitureForSale/", "/AutoServices/", "/AutosForSale/", "/MiscJobs/", \
		"/RentalsWanted/", "/Roommates/", "/HomeImprovement/", "/CommercialForRent/", "/ToolsForSale/", "TherapeuticMassage"]
	for i in range(10):
		for a in soup.findAll('a', attrs={'href': re.compile("^http://")}):
			url = a['href']
			if "Disclaimer" in url:		
				# Pulls out all of the classifieds:
				# /Dating, /MenSeekMen, /MenSeekWomen, /WomenSeekWomen, /WomenSeekMen, /Transgender
				url = url[:url.rfind("?")]
				url = re.sub("classifieds/Disclaimer", "", url) 
				url += "?page=" + str(i)				
				urls.add(url)

			for category in sampleCategories:
				if category in url:
					url += "?page=" + str(i)
					urls.add(url)

	return list(urls)

def getDataFromPagesInRegion():
	region = "http://losangeles.backpage.com/"
	information = urllib.urlopen(region).read()
	soup = BeautifulSoup(information, "html.parser")
	pages = getPagesFromRegion(soup, region)
	URLS = []
	for page in pages:
		page_information = urllib.urlopen(page).read()
		page_soup = BeautifulSoup(page_information, "html.parser")
		URLS.extend(url for url in getPostsOnPage(page_soup) if url not in URLS)
	url_df = pd.DataFrame(URLS)
	url_df.to_csv('../data/url_list.csv', index=False, header=False)	
	# tabulate(URLS)

getDataFromPagesInRegion()

