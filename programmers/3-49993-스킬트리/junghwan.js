/*

19. 06. 18

풀이: skill_tree 내의 skill 값의 인덱스를 배열에 저장하여 해결
가장 우선시 되어야 하는 스킬이 존재하는 경우에, 인덱스를 비교하여 스킬 사용 여부 판단

2019. 06. 17 - 오답(최고점수 57.1): 스킬트리 내에 스킬이 없는 경우 indexOf() 메서드는 인덱스 값이 아닌
-1을 반환한다. 따라서 check 값이 [2, 3, -1]이라면 true를 반환해야 하지만, 3 과 -1 비교를 하는 과정에서
예외처리에 걸려서 false를 반환해버렸다. 다른 예외처리에서도 잘못된 부분이 있겠지만, 이 부분이 제일 크게 작용한
것으로 보임

2019. 06. 18 - 정답
-1 값을 30으로 변환하여 대소 비교함

 */

function solution(skill, skill_trees) {
    var answer = 0;
    var s = skill;
    var st = skill_trees;

    // 스킬트리의 요소들을 하나씩 검사하여 boolean 요소들로 이루어진 배열 반환
    var result = st.reduce((acc, cur) => {
        var check = []; // skill treee 안에 skill 요소들의 인덱스를 담아줄 배열

        for(let i=0; i<s.length; i++) {
            check.push(cur.indexOf(s[i]));
        } // skill 요소들의 인덱스 저장 ex) skill="CBD", skill_tree="AECB" => check=[2, 3, -1]

        if(check.filter(i => i === -1).length === s.length) {
            acc.push(true);
            return acc;
        } // 만약 스킬트리에 스킬이 전부 없으면 -> 무조건 참

        // 스킬이 하나라도 스킬트리 안에 존재하면
        else {

            if(check[0] === -1) {
                acc.push(false);
                return acc;
            } // 스킬이 하나라도 존재하는데, 첫 번째 스킬이 없으면 -> 무조건 false

            // 스킬이 하나라도 있고, 첫 번째 스킬이 존재하는 경우
            else {
                // AECB -> check = [2, 3, -1]  true  [2, 3 ,30]
                // BACDE  -> check = [2, 0, 3]  false [2, 0, 3]
                // AC -> check = [1] true [1]
                var flag = true;

                var check2 = check.map(c => {
                    if(c === -1) { return 30;}
                    else { return c; }
                }); // 인덱스 대소비교를 수월하게 하기 위해 -1의 값을 30으로 변환
                // 30으로 변환해준 이유는 스킬의 최대 길이가 26이라는 문제의 조건 하에 임의로 지정

                for(let i=0; i<check2.length-1; i++) {
                    if(check2[i] > check2[i+1]) {

                        acc.push(false);
                        flag = false;
                        return acc;

                    } // 이전 값이 크면 false

                    else if(check2[i] < check2[i+1]) {
                        flag = true;
                    } // 다음 값이 크면 true

                    flag = true;
                }


                if(flag) {
                    acc.push(true);
                    return acc;
                } // 반복문을 다 돌고도 중간에 종료되지 않는다면 문제의 조건을 충족하는 스킬트리이기 때문에 추가

            }
        }

        return acc;

    }, []);

    console.log(result);

    answer = result.filter(i => i).length;
    // result 배열의 true 값 갯수가 답이다.
    // ex) 문제의 예시의 결과는 result = [false, true, true, false]
    // 따라서 true의 갯수인 2가 반환 -> answer

    return answer;
}