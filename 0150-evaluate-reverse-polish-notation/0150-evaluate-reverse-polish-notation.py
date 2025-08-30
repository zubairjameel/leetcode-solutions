class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif c == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif c == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            elif c == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))   # truncate toward zero
            else:
                stack.append(int(c)) 
        return stack[-1]

                
                
        