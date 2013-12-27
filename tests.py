'''
	Some little tests to see if things I consider "more shuffled" are actually considered more shuffled by the program
'''

import unittest
import shufflednessChecker


class ShufflednessTester(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testUnshuffled(self):
		deck = range(52)
		self.assertTrue(shufflednessChecker.shuffledness(deck) == 0)

	def testBackwards(self):
		deck = range(52)[::-1]
		self.assertTrue(shufflednessChecker.shuffledness(deck) < 0.5)

	def testCompare0(self):
		# This is false and I think the second one should be considered more shuffled (10-card chunks switching vs. 4-card chunks)
		deck0 = [11,12,13,14,15,16,17,18,19,1,2,3,4,5,6,7,8,9,10]
		deck1 = [5,6,7,8,1,2,3,4,13,14,15,16,9,10,11,12,13,14,15]
		print shufflednessChecker.countInversions(deck0)
		print shufflednessChecker.countInversions(deck1)
		self.assertTrue(shufflednessChecker.shuffledness(deck0) < shufflednessChecker.shuffledness(deck1))

	def testCompare1(self):
		# This is false and I think the second one should be considered more shuffled (swapping first and last card vs. randomizing within chunks of 5)
		deck0 = [19,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,0]
		deck1 = [0,3,1,5,2,4,7,6,11,9,10,8,15,12,14,13,16,19,17,18]
		print shufflednessChecker.countInversions(deck0)
		print shufflednessChecker.countInversions(deck1)
		self.assertTrue(shufflednessChecker.shuffledness(deck0) < shufflednessChecker.shuffledness(deck1))

	def testCompare2(self):
		deck0 = [19,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,0]
		deck1 = [0,3,1,5,2,4,7,6,11,9,10,8,15,12,14,13,16,19,17,18]


if __name__ == '__main__':
	unittest.main()