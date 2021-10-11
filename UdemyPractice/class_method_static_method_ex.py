class FixedFloat:
    def __init__(self, amt):
        self.amt = amt

    def __repr__(self):
        return f'<FixedFloat {self.amt:.2f}>'

    @classmethod
    def from_sum(cls, val1, val2):
        return cls(val1 + val2)


#number = FixedFloat(18.5746)
#print(number)

new_num = FixedFloat.from_sum(19.575, 0.789)
print(new_num)

class Euro(FixedFloat):
    def __init__(self, amt):
        super.__init__(amt)
        self.symbol = 'E'

    def __repr__(self):
        return f' <Euro {self.symbol}{self.amt:.2f}>'


money = Euro.from_sum(16.758, 9.999)
print(money)
