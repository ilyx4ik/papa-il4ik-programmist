import sys

def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue
        if expr[i] in "+-*/^()":
            tokens.append(expr[i])
            i += 1
        elif expr[i].isdigit() or expr[i] == '.':
            num = ""
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            tokens.append(num)
        else:
            raise ValueError(f"Недопустимий символ: {expr[i]}")
    return tokens

def shunting_yard(tokens):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    assoc = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}
    output = []
    stack = []
    for t in tokens:
        if t.replace('.', '', 1).isdigit():
            output.append(t)
        elif t in prec:
            while stack and stack[-1] in prec and (
                (assoc[t] == 'L' and prec[t] <= prec[stack[-1]]) or
                (assoc[t] == 'R' and prec[t] < prec[stack[-1]])
            ):
                output.append(stack.pop())
            stack.append(t)
        elif t == '(':
            stack.append(t)
        elif t == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Невідповідність дужок")
            stack.pop()
    while stack:
        if stack[-1] in "()":
            raise ValueError("Невідповідність дужок")
        output.append(stack.pop())
    return output

def eval_rpn(rpn_tokens):
    stack = []
    for t in rpn_tokens:
        if t.replace('.', '', 1).isdigit():
            stack.append(float(t))
        else:
            if len(stack) < 2:
                raise ValueError("Некоректний вираз")
            b = stack.pop()
            a = stack.pop()
            if t == '+': stack.append(a + b)
            elif t == '-': stack.append(a - b)
            elif t == '*': stack.append(a * b)
            elif t == '/': 
                if b == 0: raise ZeroDivisionError("Ділення на нуль")
                stack.append(a / b)
            elif t == '^': stack.append(a ** b)
    if len(stack) != 1:
        raise ValueError("Некоректний вираз")
    return stack[0]

def calculate(expr):
    tokens = tokenize(expr)
    rpn = shunting_yard(tokens)
    return eval_rpn(rpn)

def run_tests():
    assert calculate("3 + 4 * 2 / ( 1 - 5 ) ^ 2") == 3.5
    print("Тести пройдено")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
        return
    try:
        expr = input().strip()
        print(calculate(expr))
    except Exception as e:
        print(f"Помилка: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()