'''
풀이:
    선행 스킬 순서(인덱스를 이용)대로 스킬트리에 있는 순서 체크
 2019.06.21 - 오답(90%): (문제 제대로 안읽음) 여벌 체육복을 가져온 학생이 도난당했을 경우 해당 학생은 여벌이 없는걸로 간주
 2019.06.21 - 오답(90%): (예외처리 미흡) 위의 경우를 방지하기 위해 여벌 옷을 읽어버린 학생을 미리 리스트에서 제거함, list.remove()함수를 사용했는데 forloop안에서 remove를 사용하여 정상적으로 forloop를 순회하지 못하여 오답
 2019.06.22 - 정답: 귀찮아서.... 대충 처리... 미리 제거할 학생을 -9999로 대체
    n = 전체학생 수
    m = lost의 길이
    j = reserve의 길이
    시간복잡도: O(m*j)
    공간복잡도: O(m+j)
'''

def solution(n, lost, reserve):
    answer = 0
    len_lost = len(lost)
    for idx in range(len(lost)):
        if lost[idx] in reserve:
            reserve.remove(lost[idx])
            lost[idx] = -9999
            answer += 1

    for r in reserve:
        for l in lost:
            if l - 1 == r or l + 1 == r:
                lost.remove(l)
                answer += 1
                break

    return n - len_lost + answer
