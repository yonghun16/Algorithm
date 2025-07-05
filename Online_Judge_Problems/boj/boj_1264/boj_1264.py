'''
----------------------------------------------
Sub : [BOJ] 모음의 개수
Link: https://www.acmicpc.net/problem/1264
Tag : Python, 
Memo
----------------------------------------------
'''

while True:
    n = input()
    if(n == '#'): 
        break
    else :
        sum = 0
        sum += n.count('a') + n.count('e') + n.count('i') + n.count('o') + n.count('u')
        sum += n.count('A') + n.count('E') + n.count('I') + n.count('O') + n.count('U')

    print(sum)
