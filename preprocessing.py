import util

ENGL_STOP_WORDS = ['i','a','about','an','are','as','at','be','by','for', \
				'from','how','in','is','it','of','on','or','that','the', \
				'this','to','was','what','when','where','who','will','with','the']

CONTRACTIONS = { 
	"ain't": "am not; are not; is not; has not; have not",
	"aren't": "are not; am not",
	"can't": "cannot",
	"can't've": "cannot have",
	"'cause": "because",
	"could've": "could have",
	"couldn't": "could not",
	"couldn't've": "could not have",
	"didn't": "did not",
	"doesn't": "does not",
	"don't": "do not",
	"hadn't": "had not",
	"hadn't've": "had not have",
	"hasn't": "has not",
	"haven't": "have not",
	"he'd": "he had / he would",
	"he'd've": "he would have",
	"he'll": "he shall / he will",
	"he'll've": "he shall have / he will have",
	"he's": "he has / he is",
	"how'd": "how did",
	"how'd'y": "how do you",
	"how'll": "how will",
	"how's": "how has / how is / how does",
	"I'd": "I had / I would",
	"I'd've": "I would have",
	"I'll": "I shall / I will",
	"I'll've": "I shall have / I will have",
	"I'm": "I am",
	"I've": "I have",
	"isn't": "is not",
	"it'd": "it had / it would",
	"it'd've": "it would have",
	"it'll": "it shall / it will",
	"it'll've": "it shall have / it will have",
	"it's": "it has / it is",
	"let's": "let us",
	"ma'am": "madam",
	"mayn't": "may not",
	"might've": "might have",
	"mightn't": "might not",
	"mightn't've": "might not have",
	"must've": "must have",
	"mustn't": "must not",
	"mustn't've": "must not have",
	"needn't": "need not",
	"needn't've": "need not have",
	"o'clock": "of the clock",
	"oughtn't": "ought not",
	"oughtn't've": "ought not have",
	"shan't": "shall not",
	"sha'n't": "shall not",
	"shan't've": "shall not have",
	"she'd": "she had / she would",
	"she'd've": "she would have",
	"she'll": "she shall / she will",
	"she'll've": "she shall have / she will have",
	"she's": "she has / she is",
	"should've": "should have",
	"shouldn't": "should not",
	"shouldn't've": "should not have",
	"so've": "so have",
	"so's": "so as / so is",
	"that'd": "that would / that had",
	"that'd've": "that would have",
	"that's": "that has / that is",
	"there'd": "there had / there would",
	"there'd've": "there would have",
	"there's": "there has / there is",
	"they'd": "they had / they would",
	"they'd've": "they would have",
	"they'll": "they shall / they will",
	"they'll've": "they shall have / they will have",
	"they're": "they are",
	"they've": "they have",
	"to've": "to have",
	"wasn't": "was not",
	"we'd": "we had / we would",
	"we'd've": "we would have",
	"we'll": "we will",
	"we'll've": "we will have",
	"we're": "we are",
	"we've": "we have",
	"weren't": "were not",
	"what'll": "what shall / what will",
	"what'll've": "what shall have / what will have",
	"what're": "what are",
	"what's": "what has / what is",
	"what've": "what have",
	"when's": "when has / when is",
	"when've": "when have",
	"where'd": "where did",
	"where's": "where has / where is",
	"where've": "where have",
	"who'll": "who shall / who will",
	"who'll've": "who shall have / who will have",
	"who's": "who has / who is",
	"who've": "who have",
	"why's": "why has / why is",
	"why've": "why have",
	"will've": "will have",
	"won't": "will not",
	"won't've": "will not have",
	"would've": "would have",
	"wouldn't": "would not",
	"wouldn't've": "would not have",
	"y'all": "you all",
	"y'all'd": "you all would",
	"y'all'd've": "you all would have",
	"y'all're": "you all are",
	"y'all've": "you all have",
	"you'd": "you had / you would",
	"you'd've": "you would have",
	"you'll": "you shall / you will",
	"you'll've": "you shall have / you will have",
	"you're": "you are",
	"you've": "you have"
}

text = "Wouldn't you like to start or end your dayl with a relaxing massage before heading off to your final destination? Is your work week very stressful? I have just the relaxing tranquil private environment that can ease you through the rest of your day. I use nice high quality products, always fresh clean sheets and towels, a warm shower along with a very comfortable massage table. Now let me also say, I am equally at ease whether you wish to be draped or whether you're more comfortable being totally natural. The room is lit by soft candlelight and soothing soft music to lull you into a dreamlike state, and best of all, I'm NEVER rush. My studio located just minutes from LAX, with plenty of street parking. As a certified professional CMT, Im train in many massage specialties, but I bet you would benefit the most from my mixer of Lomi Lomi, Swedish and Deep Tissues to help work out your body stress area. This is a service designed specially with you in mind, but please be aware this IS a private Independent facility, I am unable to accommodated walk-in appointment; please schedule your appointment with at least 2-hours notice. ARE YOU COMING FROM OUT-OF-TOWN You can schedule before your flight with my online confidential schedule form (see below for details)."

# tokens = nltk.pos_tag(nltk.word_tokenize(text))
# good_words = [w for w, wtype in tokens if wtype not in STOP_TYPES]
# print good_words

def casefolding(s):
	s = s.lower()
	return s

def expandContractions(s):
	tokenizedStr = s.split()
	for word in tokenizedStr:
		if word in CONTRACTIONS: # expand
			tokenizedStr[]		

def expandContractions(text, c_re=c_re):
    def replace(match):
        return cList[match.group(0)]
    return c_re.sub(replace, text)

def stripStopwords(s):
	tokenizedStr = s.split()
	strippedStr  = [word for word in tokenizedStr if word not in ENGL_STOP_WORDS]
	result = ' '.join(strippedStr)
	return result

def preprocess(s):
	text = casefolding(s)
	text = stripStopwords(text)
	return text

print preprocess(text)
# print text




