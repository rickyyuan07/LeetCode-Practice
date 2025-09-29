from typing import List, Dict

def evaluate(equations: List[str]) -> Dict[str, int]:
    exprs = {}
    for eq in equations:
        left, right = eq.split("=")
        var = left.strip()
        tokens = right.strip().split()
        exprs[var] = tokens

    cache = {}
    
    def eval_var(var: str) -> int:
        if var in cache:
            return cache[var]
        tokens = exprs[var]
        total = 0
        op = "+"
        for t in tokens:
            if t in {"+", "-"}:
                op = t
            else:
                if t.lstrip("-").isdigit():  # 整數
                    val = int(t)
                else:  # 變數
                    val = eval_var(t)
                if op == "+":
                    total += val
                elif op == "-":
                    total -= val
        cache[var] = total
        return total

    return {var: eval_var(var) for var in exprs}

equations = ["a = b + c", "c = 4", "b = c + 5"]
print(evaluate(equations))
# output: {'a': 13, 'c': 4, 'b': 9}