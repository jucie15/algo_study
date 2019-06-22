'''

19. 06. 22

풀이: 학생 수와 같은 길이의 배열을 생성.
체육복을 잃어버린 학생들은 -1, 여벌이 있는 학생들은 1, 해당사항 없으면 0 값을 각각 할당
-1(잃어버린 학생) 옆에 1(여벌이 있는 학생)이 있는 경우 -1은 1을 더해주고, 1은 1을 빼준다. -> 둘 다 0이 되므로 체육복 있음
이러한 과정을 거친 후 1과0의 갯수가 체육 수업을 들을 수 있는 학생의 최댓값임

'''

def solution(n, lost, reserve):
    answer = 0
    student = []
    
    for i in range(n):
        student.append(0)
        
    for i in lost:
        student[i-1] = student[i-1] -1
    
    for i in reserve:
        student[i-1] = student[i-1] +1
        
    print(student)
    
    if student[0] == -1 and student[1] == 1:
        student[0] = student[0] + 1
        student[1] = student[1] - 1
    
    if student[len(student)-1] == -1 and student[len(student)-2] == 1:
        student[len(student)-1] = student[len(student)-1] + 1
        student[len(student)-2] = student[len(student)-2] - 1
        
    for i in range(1, len(student)-1):

        if student[i] == -1 and student[i-1] == 1:
            student[i] = student[i] + 1
            student[i-1] = student[i-1] - 1
        
        if student[i] == -1 and student[i+1] == 1:
            student[i] = student[i] + 1
            student[i+1] = student[i+1] - 1
    
    cnt = 0
    print(student)
    
    for i in student:
        if i == 0 or i == 1:
            cnt = cnt + 1
            
    answer = cnt
    
    return answer