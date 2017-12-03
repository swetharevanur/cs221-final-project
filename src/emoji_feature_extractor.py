# -*- encoding: utf-8 -*-
# emoji_feature_extractor.py
# Checks if there is presense of a key emoji in the text
# i.e. one of:  
# emoji:rose
# emoji:rosette
# emoji:cherry
# emoji:cherry blossom
# emoji:growing heart
# emoji:airplane
# emoji:crown

import emoji
from preprocessing import preprocess

key_emojis = [u'🌹',u'🏵',u'🍒',u'🌸',u'💗',u'✈',u'👑']

def textHasEmoji(text):
	for word in text.split():
		if word in key_emojis:
			return 1
	return 0