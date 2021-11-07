from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        pre_skill = deque(skill)

        for skill in skill_tree:   ### 변수의 이름이 파라미터와 똑같아서, 파라미터가 들어가진다.
            if skill in pre_skill:
                k = pre_skill.popleft()  # 스킬이 뜨면 무조건 선순환 해야되니깐.
                print(skill_tree, k, skill)

                if skill != k:
                    break
        else:
            print('forelse:',skill_tree, k, skill)
            answer += 1
    return answer

print(solution(	"CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
# 선행스킬 개념을 어떻게 구현할까. -> 큐? 먼저 빠져야 된다는 것!!

# que = deque('abc')
# print('d' in que)