from collections import deque

balanced_parentheses_string = "()))((()"

'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
'''

def get_correct_parentheses(balanced_parentheses_string):
    obj = balanced_parentheses_string
    balanced_parenthesis = ''

    if obj == '': # 밑에 코드 굳이 안쓰고 리턴 가능할때 리턴 되게끔 위에 배치.
        return ''

    str_que = deque(obj) #덱에 넣었다!!
    count = 0 # u 를 뽑아 내기 위함, ( 일때 +1, ) 일때 -1
    u, v = '', ''

    while str_que: #파이썬에는 do-while문이 없기 때문에 약간 트릭을 넣어서
        k = str_que.popleft()
        if k == '(':
            count += 1
        else:# k == ')'
            count -= 1

        u += k #문자붙이기

        if count == 0: #균형잡힌 문자열이 된다면 리턴.
            break

    v = ''.join(list(str_que)) # v에도 나머지값 넣어주기

    # u 에 대해서 올바른 괄호 문자열인지 체크해야한다. 스타트가 '(' 라면은 무조건 올바른 문자열이 된다는것에 착안
    if u[0] == '(':# 올바른 문자열일때 3번과정
        balanced_parenthesis = u + get_correct_parentheses(v)
    else: #아닐때 4번과정
        balanced_parenthesis += '('
        balanced_parenthesis += get_correct_parentheses(v)
        balanced_parenthesis += ')'
        u_que = deque(u)
        u_que.popleft() #처음과
        u_que.pop() #마지막 문자열을 제거
        while u_que:
            q = u_que.popleft()
            if q == '(':
                balanced_parenthesis += ')'
            else:
                balanced_parenthesis += '('


    return balanced_parenthesis


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))