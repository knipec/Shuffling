import random
from difflib import SequenceMatcher
import scipy

length = 5
# USING:						  MANHATTAN 	DIFFLIB
# testList = [0, 1, 2, 3, 4]	# 0				1.0
# testList = [4, 3, 2, 1, 0]	# .96			0.2
# testList = [1, 2, 3, 4, 0]	# .64			0.8
# testList = [3, 0, 4, 2, 1]	# .8			0.4
# testList = [1, 2, 4, 0, 3]	# .64			0.6
# testList = [1, 2, 3, 0, 4]	# .48			0.8

# DIFFLIB
print SequenceMatcher(None, testList, sorted(testList)).ratio()

# MANHATTAN
# manhattan = lambda l: sum(abs(a-i) for i, a in enumerate(l)) / (0.5 * len(l)**2)
# print manhattan(testList)

def alignmentDist(str1, str2):
	# Seems like 4321 is random, so no.
	d = {}
	for i in range(0, len(str1)):
		d[(i, 0)] = i
	for j in range(1, len(str2)):
		d[(0, j)] = j

	for i in range(1, len(str1)):
		for j in range(1, len(str2)):
			# print i, j
			if str1[i] == str2[j]:
				cost = 0
			else:
				cost = 1
			d[(i, j)] = min(d[(i-1, j  )] + 1,
							d[(i  , j-1)] + 1,
							d[(i-1, j-1)] + cost)
			if (i > 1 and j > 1 and str1[i] == str2[j-1] and str1[i-1] == str2[j]):
				d[(i,j)] = min(d[(i, j)],
							   d[(i-2, j-2)] + cost)
	return d[(len(str1)-1, len(str2)-1)]