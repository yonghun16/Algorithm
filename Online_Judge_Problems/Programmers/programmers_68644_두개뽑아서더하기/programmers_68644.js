/*-----------------------------------------------------
Sub  : [Programmers] 두 개 뽑아서 더하기
Link : https://school.programmers.co.kr/learn/courses/30/lessons/68644
Level: 1
Tag  : JS, 
Memo
-----------------------------------------------------*/

function solution(numbers) {
    const temp = []

    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            temp.push(numbers[i] + numbers[j])
        }
    }

    const answer = [...new Set(temp)]

    return answer.sort((a, b) => a - b)
}
