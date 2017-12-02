# -*- encoding: utf8 -*-
# util.py
# Helper functions used in parsing, preprocessing, etc.
# Author: Swetha Revanur and Keanu Spies

import re
import string

# removes all punctuation
def stripPunctuation(s):
	# s = s.encode('utf8')
	regex_sub = re.sub(r"[,.;@#?!&$()*-/\\\^+\|:]+", ' ', s)
	regex_sub = re.sub(r"\s+", ' ', regex_sub)
	# return s.translate(None, string.punctuation)
	return regex_sub

# removes all alphabetical characters
def stripAlpha(s):
	newS = re.sub( '[^\\d]', "", s)	
	return newS

# removes all HTML tag artifacts
def stripTags(s):
	newS = re.sub('<[^<]+?>', '', s)
	re.split(r'\s*', newS)
	return ''.join(newS)

def stripPunctuationWithoutSpace(s):
	regex_sub = re.sub(r"[,.;@#?!&$()*-/\\\^+\|:]+", '', s)
	return regex_sub