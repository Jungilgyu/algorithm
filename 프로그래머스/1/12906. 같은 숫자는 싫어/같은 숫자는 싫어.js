function solution(arr)
{
    var answer = [];
    
    const n = arr.length
    let lastNum = -1
    for (let i = 0; i < n; i ++) {
        if (arr[i] !== lastNum) {
            answer.push(arr[i])
            lastNum = arr[i]
        }
    }
    
    return answer;
}