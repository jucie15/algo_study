/*

19. 06. 22

풀이: 학생 수와 같은 길이의 배열을 생성.
체육복을 잃어버린 학생들은 -1, 여벌이 있는 학생들은 1, 해당사항 없으면 0 값을 각각 할당
-1(잃어버린 학생) 옆에 1(여벌이 있는 학생)이 있는 경우 -1은 1을 더해주고, 1은 1을 빼준다. -> 둘 다 0이 되므로 체육복 있음
이러한 과정을 거친 후 1과0의 갯수가 체육 수업을 들을 수 있는 학생의 최댓값임

*/

function solution(n, lost, reserve) {
    var answer = 0;
    var lostFlag = [];
    var cnt = 0;
    
    for(let i=0; i<n; i++) {
        lostFlag.push(0);
    }
    console.log(lostFlag);
    
    for(let i=0; i<n; i++) {
        for(let j=0; j<lost.length; j++) {
            if(i === lost[j]-1) {
                lostFlag[lost[j]-1]--;
            }
        }
    }
    console.log(lostFlag);
    
    for(let i=0; i<n; i++) {
        for(let j=0; j<reserve.length; j++) {
            if(i === reserve[j]-1) {
                lostFlag[reserve[j]-1]++;
            }
        }
    }
    console.log(lostFlag);
    
    // -1 옆에 1 있으면 둘다 0으로 바꿔준다.
    if(lostFlag[0] === -1 && lostFlag[1] === 1) {
        lostFlag[0] = 0;
        lostFlag[1] = 0;
    }
    
    if(lostFlag[n-1] === -1 && lostFlag[n-2] === 1) {
        lostFlag[n-1] = 0;
        lostFlag[n-2] = 0;
    }
    
    for(let i=1; i<n-1; i++) {
        if(lostFlag[i] === -1 && lostFlag[i-1] === 1) {
            lostFlag[i] = 0;
            lostFlag[i-1] = 0;
        }
        
        else if(lostFlag[i] === -1 && lostFlag[i+1] === 1) {
            lostFlag[i] = 0;
            lostFlag[i+1] = 0;
        }
    }
    
    for(let i=0; i<lostFlag.length; i++) {
        if(lostFlag[i] === 0 || lostFlag[i] === 1) {
            cnt++;
        }
    }
    
    answer = cnt;
    
    return answer;
}