# -*- encoding: utf8 -*-
# preprocessing.py
# Cleans data that was fetched from Backpage
# Author: Swetha Revanur and Keanu Spies

from contraction_dict import CONTRACTIONS
from stopwords import ENGL_STOP_WORDS
from emoji_parse import emojiTokenizer
from util import stripPunctuation, stripTags
import re
import string

# text = "Wouldn't you like to start or end your day with a relaxing massage before heading off to your final destination? Is your work week very stressful? I have just the relaxing tranquil private environment that can ease you through the rest of your day. I use nice high quality products, always fresh clean sheets and towels, a warm shower along with a very comfortable massage table. Now let me also say, I'm equally at ease whether you wish to be draped or whether you're more comfortable being totally natural. The room is lit by soft candlelight and soothing soft music to lull you into a dreamlike state, and best of all, I'm NEVER rush. My studio located just minutes from LAX, with plenty of street parking. As a certified professional CMT, Im train in many massage specialties, but I bet you would benefit the most from my mixer of Lomi Lomi, Swedish and Deep Tissues to help work out your body stress area. This is a service designed specially with you in mind, but please be aware this IS a private Independent facility, I am unable to accommodated walk-in appointment; please schedule your appointment with at least 2-hours notice. ARE YOU COMING FROM OUT-OF-TOWN You can schedule before your flight with my online confidential schedule form (see below for details)."

# convert string to lowercase
def casefolding(s):
	return s.lower()

# expand contractions and remove apostrophe
def expandContractions(s):
	c_re = re.compile('(%s)' % '|'.join(CONTRACTIONS.keys()))
	def replace(match):
		return CONTRACTIONS[match.group(0)]
	return c_re.sub(replace, s)

# remove any stop words
def stripStopWords(s):
	tokenizedStr = s.split()
	strippedStr  = [word for word in tokenizedStr if word not in ENGL_STOP_WORDS]
	result = ' '.join(strippedStr)
	return result

# remove words that are one character long
def oneCharWordRemoval(s):
	return ' '.join([w for w in s.split() if len(w)>1 or w == "u" or w == "y" or w == "r"])

# replace numbers in the middle of a word with letters (i.e. y0u -> you)
def leetTranslator(s):
	def replaceNum(num):
		if num == "0":
			return "o"
		elif num == "1":
			return "i"
		elif num == "2":
			return "z"
		elif num == "3":
			return "e"
		elif num == "4":
			return "a"
		elif num == "5":
			return "s"
		elif num == "6":
			return "g"
		elif num == "7":
			return "l"
		elif num == "8":
			return "b"
		elif num == "9":
			return "p"
	
	tokenizedStr = s.split()
	translatedStr = []
	# to make sure phone numbers, addresses, etc. aren't affected
	for word in tokenizedStr:
		if word.isalpha(): # all alphabetic
			translatedStr.append(word)
			continue 
		prevLetter = None
		nextLetter = None
		for letterIndex in range(len(word)):
			currLetter = word[letterIndex]
			if letterIndex == 0:
				prevLetter = None
				nextLetter = word[letterIndex + 1]
			elif letterIndex == len(word) - 1:
				prevLetter = word[letterIndex - 1]
				nextLetter = None
			else:
				prevLetter = word[letterIndex - 1]
				nextLetter = word[letterIndex + 1]
			if currLetter.isdigit():

				if prevLetter == None and nextLetter != None:
					if nextLetter.isalpha():
						word = word[:letterIndex] + replaceNum(currLetter) + word[letterIndex + 1:]
				elif nextLetter == None and prevLetter != None: 
					if prevLetter.isalpha():
						word = word[:letterIndex] + replaceNum(currLetter) + word[letterIndex + 1:]
				elif prevLetter.isalpha() or nextLetter.isalpha(): 
					word = word[:letterIndex] + replaceNum(currLetter) + word[letterIndex + 1:]
		translatedStr.append(word)

	return ' '.join(translatedStr)

def stripPhoneNumbers(s):
	regex_sub = re.sub(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', ' ', s)
	return regex_sub

def preprocess(s):
	text = stripTags(s)
	text = casefolding(text) # working
	text = expandContractions(text)
	text = stripPhoneNumbers(text)
	text = stripPunctuation(text)
	text = oneCharWordRemoval(text)
	# text = leetTranslator(text)
	text = emojiTokenizer(text)	# working
	text = stripStopWords(text)
	text = ' '.join(text.split())
	return text

# with open('./small_test.txt', 'r') as myfile:
# 	text=myfile.read().replace('\n', '')
# preprocess(text)

