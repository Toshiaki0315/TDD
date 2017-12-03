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
# ■ DollarとFrancの重複
# ■ equalsの一般化
# ■ timesの一般化
# ■ FrancとDollarを比較する
# ■ 通貨の概念
# ■ testFrancMultiplicationを削除する？

import unittest
from Money import Money

class MoneyTest(unittest.TestCase):
  
    def testMultiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))
  
    def testEquality(self):
        self.assertTrue(Money.dollar(5).__eq__(Money.dollar(5)))
        self.assertFalse(Money.dollar(5).__eq__(Money.dollar(6)))
        self.assertFalse(Money.franc(5).__eq__(Money.dollar(5)))

    def testCurrency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())
    
if __name__ == '__main__':
    unittest.main()
