from operator import add, mul, sub
from operator import truediv as div
from typing import List

def prefix_evaluate(prefix_evaluation: List[str]) -> int:
    stack = []

    prefix_evaluation = prefix_evaluation.split() if isinstance(prefix_evaluation, str) else prefix_evaluation 

    for token in reversed(prefix_evaluation): 
        if token.isdigit(): 
            stack.append(int(token)) 
        else: 
            if token in "+-*/": 
                operand1 = stack.pop() 
                operand2 = stack.pop() 
 
                if token == "+": 
                    result = add(operand1, operand2) 
                elif token == "-": 
                    result = sub(operand1, operand2) 
                elif token == "*": 
                    result = mul(operand1, operand2) 
                elif token == "/": 
                    result = div(operand1, operand2) 
 
                stack.append(result) 
 
    return stack[0] 
 


def to_prefix(prefix_evaluation: str) -> List[str]:
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2} 
    operators = set("+*-/") 
    output = [] 
    stack = [] 
 
    for token in reversed(prefix_evaluation.split()): 
        if token.isdigit(): 
            output.append(token) 
        elif token in operators: 
            while stack and stack[-1] != ")" and precedence[token] <= precedence.get(stack[-1], 0): 
                output.append(stack.pop()) 
            stack.append(token) 
        elif token == ")": 
            stack.append(token) 
        elif token == "(": 
            while stack and stack[-1] != ")": 
                output.append(stack.pop()) 
            stack.pop() 
 
    while stack: 
        output.append(stack.pop()) 
 
    return list(reversed(output)) 
 
def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
