from entropy import shannonEntropy
from voice import third_pov_keywords, first_pov_keywords

def featureExtractor(text):
	sparseVec = {}
	sparseVec['thirdPersonLanguage'] = isThirdPerson(text)
	sparseVec['firstPersonPlurals'] = hasFirstPersonPlural(text)
	sparseVec['kolmogorovComplexity'] = shannonEntropy(text)
	sparseVec['multipleVictimsAdvertised'] = multipleVictimsAdvertised(texts)

featureExtractor('they went to the store with us')
