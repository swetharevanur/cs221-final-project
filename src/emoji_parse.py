# -*- encoding: utf8 -*-

# emoji_parse.py
# Parser to identify emojis in text, convert to readable format, and pad with spaces
# Authors: Swetha Revanur and Keanu Spies

import util
import re
from emoji_dict import EMOJIS
import emoji as emojilibrary

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
	# sen = byteOrdering.decode('unicode-escape')
	# for i in range(1, len(sen)):
	# 	# if sen[i].isspace() or sen[i-1].isspace():
	# 	# 	continue
	# 	# if sen[i-1].isalnum() and not sen[i].isalnum():
	# 	# 	sen = sen[:i] + ' ' + sen[i:]
	# 	# 	continue
	# 	# if not sen[i-1].isalnum() and sen[i].isalnum():
	# 	# 	sen = sen[:i] + ' ' + sen[i:]
	# 	# 	continue
	# 	# print sen
	# 	sen = sen[:i] + ' ' + sen[i:]
	# 	i += 1

	# byteOrdering
	print sen
	newSen = ''
	for i in range(1, len(sen)):
		# print sen[i]
		if sen[i].isspace():
			newSen = sen[i]
		elif sen[i].isalnum() and sen[i-1].isalnum():
			newSen = sen[i]
		else:
			newSen = sen[i] + ' '

	return newSen.decode('unicode-escape')

# replaces all emojis in a string with keywords associated with each emoji
def replaceEmojis(s):	
	new_words = []	
	# s = s.encode('utf8')
	s = emojiTokenizer(s)
	s = s.encode('utf8')
	words = s.split()
	for word in words:
		if word in EMOJIS:
			new_words.append(EMOJIS[word])	
		else:
			new_words.append(word)
	return ' '.join(new_words)

print emojiTokenizer('ke🎀❤️🍅🐒🎀jjj💞lk👩🏽‍🎓k')