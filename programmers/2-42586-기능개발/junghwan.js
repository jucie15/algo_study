function solution(progresses, speeds) {
    var answer = [];
    var p = progresses;
    var s = speeds;
    var day = [];

    // 배포까지 남은 일수 계산
    for(let i=0; i<p.length; i++) {
        // (100-93) / 1
        let deployDay = 0;
        if((100-p[i]) % s[i] !== 0) {
            deployDay = parseInt((100-p[i])/s[i]) + 1;
        }
        else {
            deployDay = parseInt((100-p[i])/s[i]);
        }
        day.push(deployDay);
    } //[7,3,9]

    console.log(day);

    let cnt = 0;
    let idx = 0;
    let i = 0;

    while(idx < day.length) {
        cnt = 1; // 기본값은 1

        // 자기 자신 다음 값부터 차례대로 비교
        for(i=idx+1; i<day.length; i++) {
            if(day[idx] < day[i]) { // 다음 값이 크면
                answer.push(cnt); 
                break;
                // answer에 cnt 값 삽입 후 반복문 종료
            }
            
            // 작으면 배포일수 증가
            cnt++;
        }

        // 인덱스 변경
        idx = i;

        console.log(`cnt: ${cnt}`);
        console.log(`idx: ${idx}`);
        console.log('');
    }

    answer.push(cnt);

    //[7,9,3]
    return answer;
}