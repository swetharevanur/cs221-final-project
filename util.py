# util.py
# Helper functions
# Author: Swetha Revanur

import re

def stripPunctuation(s):
	newS = re.sub(r'[^\w\s]', '', s)
	re.split(r'\s*', newS)
	return ''.join(newS)

def stripAlpha(s):
	newS = re.sub( '[^\\d]', "", s)	
	return newS

def stripTags(s):
	newS = re.sub('\</*\w*\>', '', s)
	re.split(r'\s*', newS)
	return ''.join(newS)
