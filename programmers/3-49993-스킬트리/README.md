### 해설

skill_trees의 길이 m만큼 순회를 하면서 각각의 원소(skill_tree)에 skill에 해당되는 요소를 검사한 후 해당되는 문자가 있을 시 인덱스를 저장한다.

이 과정에서  skill_tree 내에 skill 유무 및 스킬 사용 여부를 검사할 때 skill_tree 당 n 회의 검사를 진행한다.

따라서 전체 순회의 시간복잡도를 고려하자면 `O(n*m*j)` 가 되겠다.



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

