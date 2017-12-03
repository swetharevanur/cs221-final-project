# entropy.py
# Shannon entropy computation to assess complexity of posts.
# Adapted from: https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
# Authors: Swetha Revanur and Keanu Spies

import math
from collections import Counter

def shannonEntropy(data, unit='natural'):
	base = {
		'shannon' : 2.,
		'natural' : math.exp(1),
		'hartley' : 10.
	}

	if len(data) <= 1:
		return 0

	counts = Counter()

	for d in data:
		counts[d] += 1

	probs = [float(c) / len(data) for c in counts.values()]
	probs = [p for p in probs if p > 0.]

	ent = 0

	for p in probs:
		if p > 0.:
			ent -= p * math.log(p, base[unit])

	return ent