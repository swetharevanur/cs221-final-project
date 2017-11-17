# -*- encoding: utf-8-*-

# util.py
# Helper functions used in parsing, preprocessing, etc.
# Author: Swetha Revanur and Keanu Spies



import re
import string

# removes all punctuation
def stripPunctuation(s):
	s = s.decode('unicode-escape').encode('utf8')
	return s.translate(None, string.punctuation)

# removes all alphabetical characters
def stripAlpha(s):
	newS = re.sub( '[^\\d]', "", s)	
	return newS

# removes all HTML tag artifacts
def stripTags(s):
	newS = re.sub('\</*\w*\>', '', s)
	re.split(r'\s*', newS)
	return ''.join(newS)