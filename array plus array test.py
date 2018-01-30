from code-katas import array_plus_array

import unittest
"""
Test.assert_equals(array_plus_array([1, 2, 3], [4, 5, 6]), 21)
Test.assert_equals(array_plus_array([-1, -2, -3], [-4, -5, -6]), -21)
Test.assert_equals(array_plus_array([0, 0, 0], [4, 5, 6]), 15)
Test.assert_equals(array_plus_array([100, 200, 300], [400, 500, 600]), 2100)

"""

class TestIt(unittest.TestCase):
	def test_1(self):
		self.assertEqual(array_plus_array([1, 2, 3], [4, 5, 6]), 21)
	def test_2(self):
		self.assertEqual(array_plus_array([-1, -2, -3], [-4, -5, -6]), -21)
	def test_3(self):
		self.assertEqual(array_plus_array([0, 0, 0], [4, 5, 6]), 15)
	def test_4(self):
		self.assertEqual(array_plus_array([100, 200, 300], [400, 500, 600]), 2100)
	def test_5(self):
		self.assertEqual(array_plus_array([10, 3, 2], [4, 6, 3]), 28)
	def test_6(self):
		self.assertEqual(array_plus_array([3, 20, 7], [6, 3, 1]), 40))
	def test_7(self):
		self.assertEqual(array_plus_array([2,10,8], [2, 4, 5]), 31)
	def test_8(self):
		self.assetEqual(array_plus_array([3, 7, 30], [1, 7, 9]), 57)

	
if __name__ == '__main__':
	unittest.main()