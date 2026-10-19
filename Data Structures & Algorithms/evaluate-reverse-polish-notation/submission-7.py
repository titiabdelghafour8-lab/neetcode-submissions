from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        operations = {"/", "+", "*", "-"}
        eval_stack = deque()
        for i in range(n):
            if tokens[i] not in operations:
                eval_stack.append(int(tokens[i]))
            else:
                eval_stack.append(
                    self.eval_arithmetic(
                        eval_stack.pop(), 
                        eval_stack.pop(), 
                        tokens[i])
                    )
        return eval_stack.pop()

    def eval_arithmetic(self, b: int, a: int, operation) -> int:
        if operation == "+":
            return a + b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return int(a / b)
        elif operation == "-":
            return a - b

    
