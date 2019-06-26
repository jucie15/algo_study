/*

19. 06. 26

풀이: 순열을 이용하여 모든 경우를 추출해 소수 판단 후, 소수인 경우 배열에 담아 최종적으로 배열의 길이 반환

오답: 계속해서 50점이 나왔었다 -> ex) numbers='1234' 인 경우, 1243 과 같은 케이스의 검사가 이루어지지 않았다.

 */

let answer = [];
function solution(numbers) {
    numbers = numbers.split("");
    for(let k = 1; k <= numbers.length; k++){
        permutation(numbers, 0, k);
    }
    return answer.reduce((acc,v)=>{
      if(acc.indexOf(v) == -1){
          acc.push(v)
      }
      return acc;
    },[]).length;
}


function permutation(arr, n, k){
  if(n === k){
    let number = makeNumber(arr, k);
    if(isPrimeNumber(number)){
        answer.push(number);
    }
    return;
  }

  for(let i = n; i < arr.length; i++){
    swap(arr, i, n);
    permutation(arr, n+1,k);
    swap(arr, i, n);
  }
}

function swap(arr, a, b){
  if(a === b) return;
  let tmp = arr[a];
  arr[a] = arr[b];
  arr[b] = tmp;
}

function isPrimeNumber(n){
  if(n == 0 || n == 1) return false;
  let sqrt = Math.sqrt(n);
  for(let i = 2; i <= sqrt; i++){
      if(n % i == 0){
          return false;
      }
  }
  return true;
}

function makeNumber(arr, k){
  let number = 0;
  for(let i = 0; i < k; i++){
    number += arr[i] * Math.pow(10,i);
  }
  return number;
}