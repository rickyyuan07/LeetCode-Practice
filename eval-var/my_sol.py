from typing import List, Dict

def evaluate(equations: List[str]) -> Dict[str, int]:
    expr = {}  # var: tokens
    for eq in equations:
        ll = eq.split("=")
        key = ll[0].strip()
        values = ll[1].strip().split(' ')
        expr[key] = values

    cache = {}
    def evaluate(var):
        if var in cache:
            return cache[var]

        tokens = expr[var]
        ans = 0
        opr = "+"
        for token in tokens:
            val = 0
            if token == "-":
                opr = "-"
            elif token == "+":
                opr = "+"
            elif token.isdecimal():
                val = int(token)
            else:
                val = evaluate(token)
            if opr == "+":
                ans += val
            else:
                ans -= val
        
        cache[var] = ans
        return ans

    ret = {}
    for k, v in expr.items():
        ret[k] = evaluate(k)
    return ret


equations = ["a = b + c", "c = 40", "b = c + 5"]
print(evaluate(equations))
# output: {'a': 85, 'c': 40, 'b': 45}