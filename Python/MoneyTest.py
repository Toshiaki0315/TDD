# Todo リスト
# □ $5 + 10CHF = $10(レートが2:1の場合)
# ■ $5 * 2 = $10
# ■ amountをprivateにする
# ■ Dollarの副作用どうする？
# □ moneyの丸め処理どうする？
# ■ equals()
# □ hashCode()
# □ nullとの比較
# □ 他オブジェクトとの等価性比較
# ■ 5 CHF * 2 = 10 CHF
# □ DollarとFrancの重複
# ■ equalsの一般化
# □ timesの一般化
# □ FrancとDollarを比較する

import unittest
from Dollar import Dollar
from Franc import Franc

class MoneyTest(unittest.TestCase):
  
    def testMultiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))
  
    def testEquality(self):
        self.assertTrue(Dollar(5).__eq__(Dollar(5)))
        self.assertFalse(Dollar(5).__eq__(Dollar(6)))
        self.assertTrue(Franc(5).__eq__(Franc(5)))
        self.assertFalse(Franc(5).__eq__(Franc(6)))
        self.assertFalse(Franc(5).__eq__(Dollar(5)))

    def testFrancMultiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))


if __name__ == '__main__':
    unittest.main()
