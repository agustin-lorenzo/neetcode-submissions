class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                num1, num2 = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(num1 + num2)
                elif t == '-':
                    stack.append(num2 - num1)
                elif t == '*':
                    stack.append(num1 * num2)
                elif t == '/':
                    stack.append(int(float(num2) / float(num1)))
        
        return stack[0]