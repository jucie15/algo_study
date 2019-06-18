def solution(skill, skill_trees):
    tmp_idx = -1
    flag = True
    answer = 0
    cnt = 0

    for st in skill_trees:
        flag = True
        tmp_idx = -1
        for s in skill:
            if s in st:
                i = st.index(s)
                if tmp_idx == -1:
                    tmp_idx = st.index(s)
                elif tmp_idx > i:
                    print('false', st)
                    flag = False
                    break
            else:
                i = skill.index(s)
                if i == 0:
                    flag = False
                    break
        if flag:
            print(st)
            answer += 1

    return answer
