# voice.py
# Checks for the presence of third-person language or 
# first-person plural pronouns.
# Authors: Swetha Revanur and Keanu Spies

third_pov_keywords = ['he', 'him', 'his', 'she', 'her', 'hers', 'they']
first_pov_keywords = ['we', 'our', 'ours']

def isThirdPerson(s):
	return 1 if any(key in s.split(' ') for key in third_pov_keywords) else 0

def hasFirstPersonPlural(s):
	return 1 if any(key in s.split(' ') for key in first_pov_keywords) else 0

s = "Very Large Spa - 7 Massage Rooms! Never Rushed Customer ALWAYS gets complete time \
they paid for We have full-time manager Girls never Interrupt \
massage Girls don't answer phone during massage Girls \
don't come out of room and interrupt massage We are Open Early 9am \
and Open late Many Repeat Customers!! You Can Choose the Girl \
No Old Ladies Here \
We Just remodel on September 1st \
We added more rooms because so many customers!! \
Very Clean Upscale Facilities"

print s
print isThirdPerson(s)
print hasFirstPersonPlural(s)
