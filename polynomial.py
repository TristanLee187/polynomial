class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x):
        return x


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, x):
        return self.i


def parentheses_term(p):
    return not (isinstance(p, X) or isinstance(p, Int))


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if parentheses_term(self.p2):
            return repr(self.p1) + " - ( " + repr(self.p2) + " )"
        return repr(self.p1) + " - " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if parentheses_term(self.p1):
            if parentheses_term(self.p2):
                return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if parentheses_term(self.p2):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if parentheses_term(self.p1):
            if parentheses_term(self.p2):
                return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if parentheses_term(self.p2):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) / self.p2.evaluate(x)


poly = Add(Add(Int(4), Int(3)), Add(
    X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(-1))

poly2 = Div(Mul(X(), Mul(Add(X(), Int(4)), Sub(X(), Int(4)))),
            Sub(X(), Mul(Int(2), X())))
print(poly2)
print(poly2.evaluate(-1))
