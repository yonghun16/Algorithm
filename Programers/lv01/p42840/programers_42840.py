# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = [0, 0, 0, 0]
    result = []
    student = [[1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    maxscore = 0

    for s in range(3):
        score = 0
        j = 0
        for i in range(len(answers)):
            if(s == 0):
                j = i % 5
            elif(s == 1):
                j = i % 8
            else:
                j = i % 10
            if answers[i] == student[s][j]:
                score = score + 1
        if score >= maxscore:
            maxscore = score
            answer[s] = maxscore

    for i in range(3):
        print(i, "=", answer[i])
    if answer[i] == maxscore:
        result.append(i+1)

    return result
