class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                int1, int2 = stack[-1], stack[-2]
                result = None
                if token == '+':
                    result = int1 + int2
                elif token == '-':
                    result = int2 - int1
                elif token == '*':
                    result = int1 * int2
                elif token == '/':
                    result = int(float(int2) / float(int1))
                stack.pop()
                stack.pop()
                stack.append(result)
        
        return stack[0]