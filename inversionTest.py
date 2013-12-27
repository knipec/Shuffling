def allPermutations(n):
	# Returns all permutations of numbers 0 to n-1
	if n == 1:
		return ["0"]
	oldPermutations = allPermutations(n-1)
	newPermutations = []
	for string in oldPermutations:
		for i in range(n):
			newPermutations.append(string[:i] + str(n-1) + string[i:])
	return newPermutations


def countInversions(perm):
	# Returns number of inversions in a permutation (the specific numbers don't matter, only their relationship to each other)
	inversions = 0
	for i in range(len(perm)):
		for j in range(i+1, len(perm)):
			if perm[i] > perm[j]:
				inversions += 1
	return inversions


def maxInversions(n):
	# Returns the max number of inversions for a given n
	answer = 0
	for i in range(n):
		answer += i
	return answer


def inversionDistribution(n):
	# For each number of inversions, returns the number of permutations of n elements with that many inversions
	distro = {}
	for perm in allPermutations(n):
		numInversions = countInversions(perm)
		if numInversions not in distro:
			distro[numInversions] = 0
		distro[numInversions] += 1
	return distro


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


def numPermutations(n):
	return reduce(lambda x,y: x*y, range(1, n+1))


def getMaxCoefficient(n):
	# This is the max coefficient for n = 52:
	# maxCoefficient = 505196616699593180342002521618930465247953555278076516348517981444
	maxCoefficient = 0
	for coefficient in mahonianRow(n):
		if coefficient > maxCoefficient:
			maxCoefficient = coefficient
	return maxCoefficient	


def getDistribution(n):
	# Divides each mahonian row by its max coefficient. 
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


def shuffledness(deck):
	distribution = getDistribution(len(deck))
	numInversions = countInversions(deck)
	return distribution[numInversions]


print getDistribution(52)[1], getDistribution(52)[-1]