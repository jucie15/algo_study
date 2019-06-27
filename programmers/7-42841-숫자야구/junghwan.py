'''

19. 06. 27

풀이: 123 ~ 987 까지의 수들을 하나의 리스트에 넣어서 하나씩 baseball에 들어온 리스트의 조건과 비교하여
모두 조건을 만족할 시(스트라이크와 볼의 조건이 일치) answer의 값을 증가시켜준다.

123~987까지 넣은 이유? 988부터는 중복되는 숫자가 있기 때문, 123~987 사이에 0이나 중복되는 숫자가 있는 수는 제외하고
리스트에 삽입

brute-force 의 뜻에 걸맞게 효율성은 갖다 버림

'''

def solution(baseball):
    answer = 0
    all_case = []
    flag = True
    
    for i in range(123, 988):
        ii = list(str(i))
        if ii[0] == ii[1] or ii[1] == ii[2] or ii[0] == ii[2] or ii[0] == '0' or ii[1] == '0' or ii[2] == '0':
            continue
        
        else:
            all_case.append(i)
            
    
    for i in all_case:
        
        flag = True
        
        for j in baseball:
            att_sb = [j[1], j[2]]
            if att_sb != check_num(j[0], i):
                flag = False
        
        if flag:
            answer = answer + 1
    
    return answer

def check_num(att, num):
    a = list(str(att))
    n = list(str(num))
    sb = [0, 0]
    
    for i in range(len(a)):
        for j in range(len(n)):
            if a[i] in n:
                if a[i] == n[j] and a.index(a[i]) == n.index(n[j]):
                    sb[0] = sb[0] + 1

                elif a[i] == n[j] and a.index(a[i]) != n.index(n[j]):
                    sb[1] = sb[1] + 1
            
    return sb
    