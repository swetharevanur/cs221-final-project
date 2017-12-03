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

key_emojis = ['🌹','🏵','🍒','🌸','💗','✈','👑']

def textHasEmoji(text):
	for word in text.split():
		if word in key_emojis:
			return 1
	return 0

text = preprocess('   New 💋36DDD JaNessa ❤💦💋❤100% ReaL❤💋 💦Your Home/HoteL 💋💦❤ SenSuaL Rubs ❤💦BooBs FeTish 💋FuN❤424.219.1104')