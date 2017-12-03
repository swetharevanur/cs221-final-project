# -*- encoding: utf8 -*-
from entropy import shannonEntropy
from voice import isThirdPerson, hasFirstPersonPlural
from keyword_features import containsCountriesOfInterest, multipleVictimsAdvertised, victimWeightMentioned,presenceOfPhrasesAndWords,presenceOfSpa
from emoji_feature_extractor import textHasEmoji
from ngrams import tf_idf

def featureExtractor(text):
	sparseVec = [0]*10
	sparseVec[0] = isThirdPerson(text) #['thirdPersonLanguage']
	sparseVec[1] = hasFirstPersonPlural(text) #'firstPersonPlurals'
	sparseVec[2] = shannonEntropy(text) #'kolmogorovComplexity'
	sparseVec[3] = multipleVictimsAdvertised(text) #'multipleVictimsAdvertised'
	sparseVec[4] = containsCountriesOfInterest(text) #'containsCountriesOfInterest'
	sparseVec[5] = multipleVictimsAdvertised(text) #'multipleVictimsAdvertised'
	sparseVec[6] = victimWeightMentioned(text) #'victimWeightMentioned'
	sparseVec[7] = presenceOfPhrasesAndWords(text) #'presenceOfPhrasesAndWords'
	sparseVec[8] = presenceOfSpa(text) #'presenceOfSpa'
	sparseVec[9] = textHasEmoji(text) #'textHasEmoji'
	sparseVec.extend(tf_idf(text)) # TF-IDF top n vals
	return sparseVec
# print featureExtractor('❌ 👑 ❌ 🌑 ❌ ❌ 🌑 ❌ 👑 ❌ 🌑 ❌ nuru slides ❌ 🌑 ❌ 👑 ❌ 🌑 ❌ 38 s ❌ 🌑 ❌ 👑 ❌ 🌑 ❌ 【 come my ckd00r 】 26 love cater all needs prostate bubble baths nuru hugging kissing amp caressing hamy lee')
