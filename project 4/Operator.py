import numbers

class Operator:
    def __init__(self, op, strength):
        self.op = op
        self.strength = strength

    def getStrength(self):
        return self.strength

    # Executes the operator. Requires two arguments/parameters,
    def execute(self, left, right, debug=True ):

        if not isinstance(left, numbers.Number) or not isinstance(right, numbers.Number):
            raise TypeError ("Cannot execute operation if element is not a number")
        result = self.op(left, right)
        if debug is True:
            print("Operation: "+ self.op.__name__
                + "({:f}, {:f}) = {:f}".format(left, right, result))
        return result