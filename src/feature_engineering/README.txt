Script execution order:

1. Run feature_extractor.py to generate a feature vector for each post consisting of:
- Advertisement Language Pattern
	- third-person voice
	- first-person plural pronouns
	- Shannon entropy
	- n-grams with TF-IDF
- Words and Phrases of Interest
- Countries of Interest
- Multiple Victims Advertised
- Victim Weight
- Reference to Spa or Massage Therapy
- Presence of Emojis
2. Run filter.py to filter out posts which have a zero feature vector.
