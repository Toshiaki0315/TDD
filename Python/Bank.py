class Bank():
    def __init__(self):
        self.rates = dict()
    def reduce(self, source, to_currency):
        return source.reduce(self, to_currency)

    def addRate(self, from_currency, to_currency, rate):
        self.rates[(from_currency, to_currency)] = rate

    def rate(self, from_currency, to_currency):
        if from_currency.__eq__(to_currency) == True:
            return 1
        return self.rates[(from_currency, to_currency)]
