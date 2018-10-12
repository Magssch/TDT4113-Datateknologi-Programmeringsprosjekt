from Function import Function
from Operator import Operator
from Queue import Queue
from Stack import Stack
import numpy
import numbers
import re

class Calculator:

    def __init__(self):
        self.functions = {'EXP': Function(numpy.exp),
        'LOG': Function(numpy.log),
        'SIN': Function(numpy.sin),
        'COS': Function(numpy.cos),
        'SQRT': Function(numpy.sqrt)}

        self.operators =   {'PLUS': Operator(numpy.add, 0),
                            'MULTIPLY': Operator(numpy.multiply, 1),
                            'DIVIDE': Operator(numpy.divide, 1),
                            'MINUS': Operator(numpy.subtract, 0)}

        self.output_queue = Queue()

    def calculate(self):

        calc_stack = Stack()

        while not self.output_queue.is_empty():
            if isinstance(self.output_queue.peek(), numbers.Number): # If next element is a number, push to
                                                                     # temporary stack
                calc_stack.push(self.output_queue.pop())

            elif isinstance(self.output_queue.peek(), Function): # If next element is a function, remove one element
                                                                 # from temporary stack, execute function on this
                                                                 # element, and then push to temporary stack
                tmp = calc_stack.pop()
                func = self.output_queue.pop()
                calc_stack.push(func.execute(tmp))

            elif isinstance(self.output_queue.peek(), Operator): # If next element is an operator, remove two elements
                                                                 # from temporary stack, execute operator with these,
                                                                 # and push back to temporary stack
                tmp1 = calc_stack.pop()
                tmp2 = calc_stack.pop()
                op = self.output_queue.pop()
                calc_stack.push(op.execute(tmp1, tmp2))

        return calc_stack.pop()                                 # Retrieve final result.

    def build_queue(self, input_queue):

        op_stack = Stack()

        while not input_queue.is_empty():

            if isinstance(input_queue.peek(), numbers.Number): # If input is a number, push directly to queue
                self.output_queue.push(input_queue.pop())

            elif isinstance(input_queue.peek(), Function): # If input is a function, push to operator-stack
                op_stack.push(input_queue.pop())

            elif input_queue.peek() == "(": # If input is left-parantheses, push to operator-stack
                op_stack.push(input_queue.pop())

            elif input_queue.peek() == ")": # If input is right-parantheses, empty operator-stack and push
                                            # contents to queue
                while not op_stack.peek() == "(":
                    self.output_queue.push(op_stack.pop())
                op_stack.pop()
                input_queue.pop()

            elif isinstance(input_queue.peek(), Operator): # If input is an operator, check for operator-precedence,
                                                           # emptying operator-stakc and pushing to queue.
                while not op_stack.is_empty() and (isinstance(op_stack.peek(), Function) or
                                                   (isinstance(op_stack.peek(), Operator) and
                                                    op_stack.peek().getStrength() >=
                                                    input_queue.peek().getStrength())):
                    self.output_queue.push(op_stack.pop())
                op_stack.push(input_queue.pop())

        while not op_stack.is_empty():
            self.output_queue.push(op_stack.pop())


    def parse_text(self, txt):
        text = txt.replace(" ", "").upper()
        input_queue = Queue()

        func_targets = "|".join(["^" + func for func in self.functions.keys()]) # Setup function-expression
        op_targets = "|".join(["^" + op for op in self.operators.keys()]) # Setup operator-expression

        while len(text) > 0:

            if text[0] == '(' or text[0] == ')': # Check if next char is a parantheses
                input_queue.push(text[0])
                text = text[1:]
            else:
                if not re.search(func_targets, text) == None: # Search for a function-expression
                    check = re.search(func_targets, text)
                    input_queue.push(self.functions[check.group(0)])

                elif not re.search(op_targets, text) == None: # Search for an operator-expression
                    check = re.search(op_targets, text)
                    input_queue.push(self.operators[check.group(0)])

                elif not re.search("^[−0123456789.]+", text) == None: # Search for a number
                    check = re.search("^[−0123456789.]+", text)
                    input_queue.push(float(check.group(0)))
                else:
                    print("Error: Unknown operator/operand/function")
                    return
                text = text[check.end(0):]

        return input_queue

    # Combines the different methods: Parse an input-text -> Build the queue -> Calculate expression
    def calculate_expression(self, text):
        self.build_queue(self.parse_text(text))
        print(self.calculate())



# Test method
if __name__ == '__main__':

    print("\nTesting __init__")
    calc = Calculator()
    print(calc.functions['EXP'].execute(
    calc.operators['PLUS'].execute(
    1, calc.operators['MULTIPLY'].execute(2, 3))))


    print("\n\nTesting calculate()")
    calc.output_queue.push(7)
    calc.output_queue.push(calc.functions['EXP'])
    print(calc.calculate())

    print("\n\nTesting build_queue()")
    calc = Calculator()
    input_queue = Queue()
    input_queue.push(calc.functions['EXP'])
    input_queue.push('(')
    input_queue.push(1)
    input_queue.push(calc.operators['PLUS'])
    input_queue.push(2)
    input_queue.push(calc.operators['MULTIPLY'])
    input_queue.push(3)
    input_queue.push(')')
    calc.build_queue(input_queue)
    print(calc.calculate())

    print("\n\nTesting parse_text()")
    calc = Calculator()

    print("\nThis should be 5:")
    calc.calculate_expression("((15 DIVIDE (7 MINUS (1 PLUS 1))) MULTIPLY 3) MINUS (2 PLUS (1 PLUS 1))")

    print("\nThis should be 1096 (ish):")
    calc.calculate_expression("EXP(1 PLUS 2 MULTIPLY 3)")
