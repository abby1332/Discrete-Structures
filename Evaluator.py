#COMP 3240 Section 001 Programming Assignment 1 Abby Miller
import copy

operators = ["~", "V", "^", ">"]
letters = "abcdefghijklmnopqrstuvwxyz"

def evaluate(argument: str, **input_value_list):
    """ Evaluates the truthfulness of the argument given the values """
    ast = parse(argument)
    return eval_rpn(ast, input_value_list)

def parse(argument: str):
    """ Turns an infix arithmetic string into an RPN representation.
        Uses the Shunting yard algorithm. This is used to resolve operator
        precedence and handle parentheses. """

    output = ""
    operator_stack = ""

    while len(argument) > 0:
        # Get the next token
        token = argument[0]
        argument = argument[1:]

        if token in operators:
            precedence = get_precedence(token)

            # Pop operators off the stack and push them into the output queue until the next operator
            # in the stack has a higher precedence (i.e. the operators popped off the stack will be
            # executed before the current operator)
            while len(operator_stack) > 0 and precedence <= get_precedence(operator_stack[-1]):
                output += operator_stack[-1]
                operator_stack = operator_stack[:-1]

            operator_stack += token
        elif token == '(':
            operator_stack += token
        elif token == ')':
            # Remove operators until the left parenthesis is found
            while operator_stack[-1] != '(':
                output += operator_stack[-1]
                operator_stack = operator_stack[:-1]
            
            # Pop the left parenthesis
            operator_stack = operator_stack[:-1]
        elif token in letters:
            output += token
        else:
            raise Exception(f"Token {token} is not a valid token")

    # Add the rest of the operators into the output in precedence order
    while len(operator_stack) > 0:
        output += operator_stack[-1]
        operator_stack = operator_stack[:-1]
    
    return output

def eval_rpn(rpn: str, vars):
    stack = []

    while len(rpn) > 0:
        token = rpn[0]
        rpn = rpn[1:]

        if token in letters:
            stack.append(vars[token])
        elif token == '^':
            operand1 = stack[-1]
            operand2 = stack[-2]
            stack = stack[:-2]

            stack.append(operand1 and operand2)
        elif token == 'V':
            operand1 = stack[-1]
            operand2 = stack[-2]
            stack = stack[:-2]

            stack.append(operand1 or operand2)
        elif token == '~':
            operand = stack[-1]
            stack = stack[:-1]

            stack.append(not operand)
        elif token == ">":
            operand1 = stack[-1]
            operand2 = stack[-2]
            stack = stack[:-2]

            stack.append((not operand2) or operand1)
    
    # Check to see if the stack length is the correct length
    if len(stack) > 1:
        raise Exception(f"Not enough operators in argument; there were {len(stack)} operands remaining")
    
    if len(stack) == 0:
        raise Exception("Error when evaluating argument. No operands remaining")

    # Return the only value on the stack (i.e., the result)
    return stack[0]

def get_precedence(token):
    """ Returns a number denoting when in the order of operations the operator
        will be calculated (i.e. * before +). Higher number -> higher precedence """

    if token == '>':
        return 0
    elif token == '^' or token == 'V':
        return 1
    elif token == '~':
        return 2
    elif token == '(' or token == ')':
        return -1
    else:
        return -5