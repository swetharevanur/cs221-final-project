# batch_parser.py
# Fetch post data from list of URLS.
# Authors: Swetha Revanur and Keanu Spies

from backpage_parser import tabulate
import csv
from time import sleep

# read web crawler csv file save to list
urls = []
with open('../data/url_list.csv', 'rb') as urlFile:
	url_list = csv.reader(urlFile, delimiter=',')	
	for row in url_list:
		urls.extend(row)

numBatches = len(urls)/100
# numBatches = 1
for batch in range(16,numBatches):
	print batch
	tabulate(urls[batch*100: batch*100 + 100], batch + 1)
	if batch != numBatches - 1:
		sleep(120)
# n = 0
# for url in urls[8*100: 8*100 + 100]:
# 	print url
# 	tabulate([url], 9)
# 	n += 1
