// https://programmers.co.kr/learn/courses/30/lessons/42840

function solution(answers) {
    var answer = [];
    var user = 
        [[1,2,3,4,5], 
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]];
    var point = [0,0,0];

    for(var i=0; i<answers.length; i++) {
        if(user[0][i%5] == answers[i])  point[0]++; 
        if(user[1][i%8] == answers[i])  point[1]++; 
        if(user[2][i%10] == answers[i]) point[2]++; 
    }

    var max = Math.max(... point);

    for(var i=0; i<3; i++) {
        if(point[i] == max) answer.push(i+1);
    }

    return answer;
}
