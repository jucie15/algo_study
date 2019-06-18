### 해설

    제공 된 스킽트리의 각 원소들을 선행스킬순서에 맞는지 문자열 인덱스를 가지고 탐색하며 순서가 맞는지 체크한다.
    BruteForce Or String 처리 문제 인 듯하다.


n = skills ( 2<= n <= 26)

m = skill_trees ( 2 <= m <= 20)

j = skill_tree (2<= j <= 26)

시간복잡도: `O(n*m*j)`

공간복잡도: `O(m)`


```python
def solution(skills, skill_trees):
    pre_st_idx = -1 # 이전에 체크한 인덱스(skill_tree)
    pre_skill_idx = -1 # 이전에 체크한 인덱스(skill)
    is_answer = True # 정답인가
    is_checked_first_skill = True # 첫번쨰 스킬은 찍었는가?
    answer = 0

    for skill_tree in skill_trees:
        # 다음 스킬트리 검사 전 변수 초기화
        is_answer = True
        is_checked_first_skill = True
        pre_st_idx = -1
        pre_skill_idx = -1
        for skill in skills:
            if skill in skill_tree:
                if is_checked_first_skill == False:
                    # 첫 번째 스킬을 안배우고 다른 스킬을 배울 경우
                    is_answer = False
                    break
                i = skill_tree.index(skill)
                if pre_st_idx == -1:
                    pre_st_idx = i
                    pre_skill_idx = skill.index(skill)
                elif pre_st_idx >= i or skill.index(skill) - pre_skill_idx >= 2:
                    # 스킬 트리 순서가 잘못 된 경우
                    is_answer = False
                    break
                else:
                    # 정상적인 스킬트리일 경우
                    pre_st_idx = i
                    pre_skill_idx = skill.index(skill)
            else:
                # 첫 번쨰 스킬을 안배운 경우 체크
                i = skill.index(skill)
                if i == 0:
                    is_checked_first_skill = False
        if is_answer:
            answer += 1

    return answer
```

