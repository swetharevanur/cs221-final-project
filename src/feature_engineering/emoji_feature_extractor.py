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
key_emojis = ['🌹','🏵','🍒','🌸','💗','✈','👑']

def textHasEmoji(text):
	return 1 if any(key_emoji in text.encode('utf8') for key_emoji in key_emojis) else 0