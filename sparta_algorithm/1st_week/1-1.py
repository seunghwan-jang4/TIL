# 팰린드롬 확인
user_input = input("문자를 입력하세요.")
n = len(user_input)
is_palindrome = True

for i in range(n // 2):
    if user_input[i] != user_input[n - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("팰린드롬입니다.")
else:
    print("팰린드롬이 아닙니다.")