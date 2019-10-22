function solution(numbers) {
    var answer = '';
    var ns = numbers.map(e => e.toString());
    
    ns.sort((a, b) => {
        var sum = a + b;
        var reverseSum = b + a;
        
        if(sum >= reverseSum) {
            return -1;
        }
        
        else {
            return 1;
        }
    });
    
    answer = ns.join('');
    
    if(ns[0] === '0') {
        ns.shift();
    }
    
    let cnt = 0;
    for(let i=0; i<ns.length; i++) {
        if(ns[i] === '0') {
            cnt++;
        }
    }
    
    if(cnt === ns.length) {
        answer = '0';
    }
    
    
    return answer;
}