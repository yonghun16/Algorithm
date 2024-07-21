// https://programmers.co.kr/learn/courses/30/lessons/12977

function solution(nums) {
    let nums_len = nums.length;
    let answer = 0;

    for (let i = 0; i < nums_len - 2; i++) {
        for (let j = i + 1; j < nums_len - 1; j++) {
            for (let k = j + 1; k < nums_len; k++) {
                if (lsPrime(nums[i], nums[j], nums[k])) {
                    answer++;
                }
            }
        }
    }
    return answer;
}

function lsPrime(a, b, c) {
    let sum = a + b + c;
    for (let i = sum - 1; i > 1; i--) {
        if (sum % i == 0) {
            return false;
        }
    }
    return true;
}
