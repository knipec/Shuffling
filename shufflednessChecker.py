'''
	Checks "how shuffled" a list of numbers is based on Mahonian triangles 
	(This question was really helpful: http://stackoverflow.com/questions/19372991/number-of-n-element-permutations-with-exactly-k-inversions)
'''

def shuffledness(deck):
	'''Returns a float between 0 and 1, where 0 is the sorted deck, and 1 is considered well-shuffled'''
	distribution = getDistribution(len(deck))
	numInversions = countInversions(deck)
	return distribution[numInversions]


def countInversions(perm):
	'''Returns number of inversions in a permutation (the specific numbers don't matter, only their relationship to each other)'''
	inversions = 0
	for i in range(len(perm)):
		for j in range(i+1, len(perm)):
			if perm[i] > perm[j]:
				inversions += 1
	return inversions


def mahonianRow(n):
	'''Generates coefficients in expansion of Product_{i=0..n-1} (1+x+...+x^i)
	code from http://stackoverflow.com/questions/19372991/number-of-n-element-permutations-with-exactly-k-inversions'''
	row = 1
	oldList = [1]
	while row < n:
		row += 1
		multList = [1] * row
		newList = [0] * (1 + row*(row-1)/2)
		for i in range(len(oldList)):
			for j in range(len(multList)):
				newList[i+j] += oldList[i] * multList[j]
		oldList = newList[:]
	return newList


def getMaxCoefficient(n):
	'''Each entry in a mahonian triangle row is a coefficient for a polynomial expansion. This returns the largest coefficient for the nth mahonian row'''
	# This is the max coefficient for n = 52:
	# maxCoefficient = 505196616699593180342002521618930465247953555278076516348517981444
	maxCoefficient = 0
	for coefficient in mahonianRow(n):
		if coefficient > maxCoefficient:
			maxCoefficient = coefficient
	return maxCoefficient	


def getDistribution(n):
	'''Divides each mahonian row by its max coefficient and returns the resulting list'''
	# This means 0 means very "un-shuffled" (or an uncommon number of inversions)
	# and 1 means most "shuffled" (or a common number of inversions)
	maxCoefficient = getMaxCoefficient(n)
	newMahonian = mahonianRow(n)
	# A permutation exactly in order should return 0
	# Also maybe one from backwards is a little more "shuffled" than one from sorted
	firstCoefficient = newMahonian[0]
	for i in range(len(newMahonian)/2):
		newMahonian[i] -= firstCoefficient
	return map(lambda x: float(x)/maxCoefficient, newMahonian)


if __name__ == '__main__':
# USING:						  MANHATTAN 	DIFFLIB		MAHONIAN
	testList1 = [0, 1, 2, 3, 4]	# 0				1.0			0
	testList2 = [4, 3, 2, 1, 0]	# .96			0.2			0.045
	testList3 = [1, 2, 3, 4, 0]	# .64			0.8			0.864
	testList4 = [3, 0, 4, 2, 1]	# .8			0.4 		0.909
	testList5 = [1, 2, 4, 0, 3]	# .64			0.6 		0.864
	testList6 = [1, 2, 3, 0, 4]	# .48			0.8 		0.636
	print shuffledness(testList1)
	print shuffledness(testList2)
	print shuffledness(testList3)
	print shuffledness(testList4)
	print shuffledness(testList5)
	print shuffledness(testList6)
