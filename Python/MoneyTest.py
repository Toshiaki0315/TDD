# Todo リスト
# □ $5 + 10CHF = $10(レートが2:1の場合)
# □ $5 * 2 = $10
import unittest
from Dollar import Dollar

class MoneyTest(unittest.TestCase):
  
    def testMultiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount)

if __name__ == '__main__':
    unittest.main()