#! python3
# -*- encoding: utf8 -*-

# emoji_parse.py
# Parser to identify emojis in text, convert to readable format, and pad with spaces
# Authors: Swetha Revanur and Keanu Spies

import util
import re
from emoji_dict import EMOJIS

# pads emojis that are consecutive without intermediate characters
def emojiTokenizer(s):
	# converts bytes to unicode
	byteOrdering = s.decode('utf8').encode('unicode-escape')
	
	# removes alphabetic character
	index = byteOrdering.find('\\')
	sen = byteOrdering[:index]
	byteOrdering = byteOrdering[index:]
	
	# finds indexes of unicode backslashes
	backslashIndexes = [m.start() for m in re.finditer(r'\\', byteOrdering)]

	for i in range(len(backslashIndexes)):
		index = backslashIndexes[i]
		if i == len(backslashIndexes) - 1:
			sen += ' ' + byteOrdering[index:].decode('unicode-escape')
			break
		nextindex = backslashIndexes[i + 1]
		sen += ' ' + byteOrdering[index:nextindex].decode('unicode-escape')

	# handles edge cases like eee<word> and e<word>e<word>e
	if sen: 
		newSen = sen[0]
		for i in range(1, len(sen)):
			if sen[i].isalnum():
				if not sen[i-1].isalnum() and not sen[i-1].isspace():
					newSen += ' ' + sen[i]
				else:
					newSen += sen[i]	
			else: 
				newSen += sen[i]

		return newSen
	return sen

# replaces all emojis in a string with keywords associated with each emoji
# def replaceEmojis(s):	
# 	new_words = []	
# 	# s = s.encode('utf8')
# 	s = emojiTokenizer(s)
# 	s = s.encode('utf8')
# 	words = s.split()
# 	for word in words:
# 		if word in EMOJIS:
# 			new_words.append(EMOJIS[word])	
# 		else:
# 			new_words.append(word)
# 	return ' '.join(new_words)

# print emojiTokenizer('ke🎀❤️🍅🐒🎀jjj💞lk👩🏽‍🎓k')