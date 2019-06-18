'''
풀이:
    선행 스킬 순서(인덱스를 이용)대로 스킬트리에 있는 순서 체크
 2019.06.17 - 오답(50%): (예외처리 미흡) 순서와 상관 없는 다른 스킬만 배울 경우와 첫 번쨰 스킬을 안 배울 경우 예외처리 안함.
 2019.06.14 - 정답
    n = skills의 길이
    m = skill_trees의 길이
    시간복잡도: O(n*m^2)
    공간복잡도: O(m)
'''
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
