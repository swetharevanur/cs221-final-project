# -*- encoding: utf-8-*-
# pip install emoji

import util
import re
from emoji_dict import EMOJIS
import emoji as emojilibrary

# TODO: eee<word> and e<word>e<word>e

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
	return sen

print emojiTokenizer("back😂🍅🐒")

# def replaceEmojis(s):	
# 	new_words = []
# 	words = s.split()
# 	print words
# 	for word in words:
# 		if word in EMOJIS:
# 			new_words.append(EMOJIS[word])	
# 		else:
# 			new_words.append(word)

# 	return ' '.join(new_words)

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

