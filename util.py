# util.py
# Helper functions
# Author: Swetha Revanur

import re

def stripPunctuation(s):
	newS = re.sub(r'[^\w\s]', '', s)
	re.split(r'\s*', newS)
	return ''.join(newS)
