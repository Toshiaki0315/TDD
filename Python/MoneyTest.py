# Todo リスト
# ■ $5 + 10CHF = $10(レートが2:1の場合)
# ■ $5 + $5 = $10
# □ $5 + $5がMoneyを返す
# ■ Bank.reduce(Money)
# ■ Moneyを変換して換算を行う
# ■ Reduce(Bank, String)
# □ Sum.plus
# □ Expression.times 
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
from Sum import Sum
from Money import Money
from Bank import Bank

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
    
    def testSimpleAddition(self):
        five = Money.dollar(5)
        ｓ = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(s, "USD")
        self.assertEqual(Money.dollar(10), reduced)

    def testPlusReturnsSum(self):
        five = Money.dollar(5)
        result = five.plus(five)
        s = result
        self.assertEqual(five, s.augend)
        self.assertEqual(five, s.addend)
    
    def testReduceSum(self):
        s = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(s, "USD")
        self.assertEqual(Money.dollar(7), result)

    def testReduceMoney(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)

    def testReduceMoneyDifferentCurrency(self):
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)
    
    def testIdentityRate(self):
        self.assertEqual(1, Bank().rate("USD", "USD"))
    
    def testMixedAddtion(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(fiveBucks.plus(tenFrancs), "USD")
        self.assertEqual(Money.dollar(10), result)
    
if __name__ == '__main__':
    unittest.main()
