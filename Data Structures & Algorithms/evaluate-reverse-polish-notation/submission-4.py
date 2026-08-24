class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand1, operand2 = 1, 1

        stack = []

        for c in tokens:
            
            
            if c == '+':
                operand1 = stack.pop()
                operand2 = stack.pop()
                res = operand2 + operand1
                stack.append(res)
            
            elif c == '-':
                operand1 = stack.pop()
                operand2 = stack.pop()
                res = operand2 - operand1
                stack.append(res)

            elif c == '*':
                operand1 = stack.pop()
                operand2 = stack.pop()
                res = operand2 * operand1
                stack.append(res)

            elif c == '/':
                operand1 = stack.pop()
                operand2 = stack.pop()
                res = (operand2) / operand1
                stack.append(int(res))
            
            else:
                stack.append(int(c))

        
        return stack[-1]