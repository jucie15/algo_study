'''
풀이:
    선행 스킬 순서(인덱스를 이용)대로 스킬트리에 있는 순서 체크
 2019.06.17 - 오답(50%): (예외처리 미흡) 순서와 상관 없는 다른 스킬만 배울 경우와 첫 번쨰 스킬을 안 배울 경우 예외처리 안함.
 2019.06.14 - 정답
    시간복잡도: ???
    공간복잡도:O(n)
'''
def solution(skill, skill_trees):
    tmp_idx = -1 # 이전에 체크한 인덱스(skill_tree)
    st_idx = -1 # 이전에 체크한 인덱스(skill)
    flag = True
    f_s_flag = True
    answer = 0

    for st in skill_trees:
        flag = True
        f_s_flag = True
        tmp_idx = -1
        st_idx = -1
        for s in skill:
            if s in st:
                if f_s_flag == False:
                    # 첫 번째 스킬을 안배우고 다른 스킬을 배울 경우
                    flag = False
                    break
                i = st.index(s)
                if tmp_idx == -1:
                    tmp_idx = i
                    st_idx = skill.index(s)
                elif tmp_idx >= i or skill.index(s) - st_idx >= 2:
                    # 스킬 트리 순서가 잘못 된 경우
                    flag = False
                    break
                else:
                    # 정상적인 스킬트리일 경우
                    tmp_idx = i
                    st_idx = skill.index(s)
            else:
                # 첫 번쨰 스킬을 안배운 경우 체크
                i = skill.index(s)
                if i == 0:
                    f_s_flag = False
        if flag:
            answer += 1

    return answer
