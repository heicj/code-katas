import unittest
#tests for kata "sum of the first nth term of series"

class testIt(unittest.TestCase):
	def test_1(self):
		self.assertEqual(series_sum(1), "1.00")
	
	def test_2(self):
		self.assertEqual(series_sum(2), "1.25")
  
  def test_2(self):
    self.assertEqual(series_sum(3), "1.39")
		
if __name__ == '__main__':
	unittest.main()
