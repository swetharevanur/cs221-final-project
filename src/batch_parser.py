# batch_parser.py
# Authors: Swetha Revanur and Keanu Spies

from backpage_parser import tabulate
import csv

# read web crawler csv file save to list
with open('../data/url_list.csv', 'rb') as urlFile:
	url_list = csv.reader(urlFile, delimiter=',')
	type(url_list)

# for batch in range(len(posts)/100):
# 	tabulate(posts[batch*100: batch*100 + 100], batch)


# 100 at a time 


