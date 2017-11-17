# emoji_parse.py
# Parser to identify emojis in text, convert to readable format, and pad with spaces
# Authors: Swetha Revanur and Keanu Spies

# -*- encoding: utf-8-*-

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
	for i in range(len(sen)):
		if sen[i].isalnum():
			sen = sen[:i] + ' ' + sen[i:]
			break

	return sen

# replaces all emojis in a string with keywords associated with each emoji
def replaceEmojis(s):	
	new_words = []	
	s = s.encode('utf8')
	s = emojiTokenizer(s)
	s = s.encode('utf8')
	words = s.split()
	for word in words:
		if word in EMOJIS:
			new_words.append(EMOJIS[word])	
		else:
			new_words.append(word)
	return ' '.join(new_words)

# def replaceEmojis(s):	
# 	new_words = []
# 	words = s.split()
# 	for i in range(len(words)):
# 		word = words[i]	
		
# 		if not word.isalpha():
# 			true_word = ''
# 			for char in word:
# 				if char.isalpha():
# 					true_word += char
# 				else
# 					break
		
# 			word = word[word.find(true_word) + len(true_word):]
# 			for key, value in EMOJIS.iteritems():
# 				if 

# 			new_words.append(EMOJIS[word])	
					
# 		else:
# 			if word in EMOJIS:
# 				new_words.append(EMOJIS[word])	
# 			else:
# 				new_words.append(word)

# 	return ' '.join(new_words)

# print emojiTokenizer("😂back🍅🐒7⃣").split(" ")

