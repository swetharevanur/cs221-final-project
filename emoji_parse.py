# -*- encoding: utf-8 -*-
# pip install emoji

import util
import re
from emoji_dict import EMOJIS
import emoji as emojilibrary

def replaceEmojis(s):	
	new_words = []
	words = s.split()
	print words
	for i in range(len(words)):
		word = words[i]	
		print word	
		if text_has_emoji(word):
			print 'yes'
			emoji_list = word.split('\\')
			for emoji in emoji_list:
				if '\\' + emoji in EMOJIS:
					new_words.append(EMOJIS[emoji])	
				else:
					new_words.append(word)

		else:
			if word in EMOJIS:
				new_words.append(EMOJIS[word])	
			else:
				new_words.append(word)

	return ' '.join(words)

def text_has_emoji(text):
    for character in text:
        if character in emojilibrary.UNICODE_EMOJI:
            return True    
        return False

# def emoji_list():
# 	apos = '"'
# 	print 'emoji_dict = { '# 	i = 0
# 	for uni, emoji in emoji_dict.iteritems():
# 		if i == 0:
# 			print 'emoji_dict = { ' + apos + str(uni)  + apos + ' : ' + apos + '_'.join(emoji.split()) + apos + ','		if i < 841:
# 			print apos + str(uni)  + apos + ' : ' + apos + '_'.join(emoji.split()) + apos + ','
# 		else:
# 			print apos + str(uni)  + apos + ' : ' + apos + '_'.join(emoji.split()) + apos		
# 		i += 1
# 	print '}'

print replaceEmojis('back\xf0\x9f\x9b\x85')

