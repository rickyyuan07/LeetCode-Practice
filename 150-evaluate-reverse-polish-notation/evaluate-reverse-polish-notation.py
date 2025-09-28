class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in "+-*/":
                rgt = stack.pop(-1)
                lft = stack.pop(-1)
                if tok == '+':
                    res = lft + rgt
                elif tok == '-':
                    res = lft - rgt
                elif tok == '*':
                    res = lft * rgt
                elif tok == '/':
                    res = int(lft/rgt)
                stack.append(res)
            else:
                stack.append(int(tok))
        
        return stack[-1]