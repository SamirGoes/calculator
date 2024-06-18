from gates import Gates
from result import Result

class Calculator:

    def __init__(self) -> None:
        pass

    def halfAdder(self, a, b):
        g = Gates()
        sum = g.XOR(a, b)
        carry = g.AND(a, b)

        return Result(sum, carry)
    
    def adder(self, a, b, c):
        g = Gates()

        halfAdder1 = self.halfAdder(a, b)
        halfAdder2 = self.halfAdder(halfAdder1.sum, c)

        xorResult = g.OR(halfAdder1.carry, halfAdder2.carry)

        return Result(halfAdder2.sum, xorResult)
    
    def getBinary(self, value):
        return "{0:b}".format(value).zfill(4)
    
    def sum(self, a, b):
        a = list(map(int, self.getBinary(a)))
        b = list(map(int, self.getBinary(b)))

        result = []
        carry = 0
        for x in range(len(a) -1, -1, -1):
            calc = self.adder(a[x], b[x], carry)
            result.append(calc.sum)
            carry = calc.carry

        return ''.join(str(x) for x in reversed(result))


        