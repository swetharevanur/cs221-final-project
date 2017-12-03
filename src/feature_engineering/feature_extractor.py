from entropy import shannonEntropy
from voice import third_pov_keywords, first_pov_keywords
from keyword_features import containsCountriesOfInterest, multipleVictimsAdvertised, victimWeightMentioned,presenceOfPhrasesAndWords,presenceOfSpa
from emoji_feature_extractor import textHasEmoji

def featureExtractor(text):
	sparseVec = {}
	sparseVec['thirdPersonLanguage'] = isThirdPerson(text)
	sparseVec['firstPersonPlurals'] = hasFirstPersonPlural(text)
	sparseVec['kolmogorovComplexity'] = shannonEntropy(text)
	sparseVec['multipleVictimsAdvertised'] = multipleVictimsAdvertised(texts)
	sparseVec['containsCountriesOfInterest'] = containsCountriesOfInterest(text)	
	sparseVec['multipleVictimsAdvertised'] = multipleVictimsAdvertised(text)
	sparseVec['victimWeightMentioned'] = victimWeightMentioned(text)
	sparseVec['presenceOfPhrasesAndWords'] = presenceOfPhrasesAndWords(text)
	sparseVec['presenceOfSpa'] = presenceOfSpa(text)
	sparseVec['textHasEmoji'] = textHasEmoji(text)
	

featureExtractor('they went to the store with us')
