import numbers
import numpy

class Function:
    def __init__(self, func):
        self.func = func

    # Executes the function.
    def execute(self, element , debug=True ):

        if not isinstance(element , numbers.Number ):
            raise TypeError ("Cannot execute func if element is not a number")
        result = self.func(element)
        if debug is True:
            print("Function: "+ self.func.__name__
                + "({:f}) = {:f}".format(element , result))
        return result

# Test method
if __name__ == '__main__':
    exponential_func = Function(numpy.exp)
    sin_func = Function(numpy.sin)
    print(exponential_func.execute(sin_func.execute(0)))