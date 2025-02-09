# 짝수, 홀수 판별
user_input = int(input('숫자를 입력하세요: '))
if user_input % 2 == 0:
    print('짝수입니다.')
elif user_input % 2 == 1:
    print('홀수입니다.')