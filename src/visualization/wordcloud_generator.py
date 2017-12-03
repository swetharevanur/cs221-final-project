# wordcloud_generator.py
# Generates wordcloud from filtered and preprocessed post text.
# Authors: Swetha Revanur and Keanu Spies

from os import path
from wordcloud import WordCloud
import glob
import pandas as pd
import matplotlib.pyplot as plt

d = path.dirname(__file__)

# import file
def importFilesAsDF():
	pathToFile =r'../../data' # use your path
	fileName = glob.glob(pathToFile + "/third_total_file_list.xlsx") # returns a list
	df = pd.read_excel(''.join(fileName)) # converts list to string
	return df

# read the relevant text
df = importFilesAsDF()

# util function
# TODO - decompose
def isFloat(string):
	try:
		float(string)
		return True
	except ValueError:
		return False

doc_set = []
for i, row in df.iterrows():
	text = df.iat[i,8]
	title = df.iat[i,10]
	# text is nan if cell is empty, so just catch and change to empty string
	if isFloat(text): text = ""
	if isFloat(title): title = ""
	currentText = text + title
	doc_set.append(currentText)

textList = []
# loop through document list
for doc in doc_set:
	print doc.split()
	textList.extend(doc.split())
text = " ".join(textList)

# generate a word cloud image
wordcloud = WordCloud().generate(text)

# display image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()