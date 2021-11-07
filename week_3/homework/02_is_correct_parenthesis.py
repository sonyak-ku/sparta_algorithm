s = "(())()"
# ())()
# ((())), ())(()
def is_correct_parenthesis(string):
    is_correct = True
    opened = 0

    for i in string:
        if opened < 0:
            return False
        if i == '(':
            opened += 1
        elif i == ')':
            opened -= 1

    if opened > 0 or opened < 0:
        is_correct = False

    return is_correct


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))