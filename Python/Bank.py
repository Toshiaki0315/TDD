from Money import Money

class Bank():
    def reduce(self, source, to):
        if(type(source) == Money):
            return source.reduce(to)
        sum = source
        return sum.reduce(to)