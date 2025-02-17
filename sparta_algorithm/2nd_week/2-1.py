def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)  # 정수 나눗셈

    return stack[0]

# 예시 입력
expression1 = "2 3 + 5 *"
expression2 = "4 2 / 3 - 2 *"

# 예시 출력
print(evaluate_postfix(expression1))  # 출력: 25
print(evaluate_postfix(expression2))  # 출력: -2