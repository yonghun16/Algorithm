'''---------------------------------------------
Sub  : [BOJ] 셀프 넘버
Link : https://www.acmicpc.net/problem/4673
Level: 실버 5
Tag  : Python, 부루트포스
Memo
 - 
---------------------------------------------'''

# 셀프 넘버 확인 함수
def is_self_number(guess_number):
    for i in range(guess_number-1, 0, -1):
        create_number = i
        for j in range(0, len(str(i))):
            create_number += int(str(i)[j])
        if create_number == guess_number:
            return False
        if create_number < guess_number-len(str(guess_number))*10:
            return True
    return True

for guess_number in range(1, 10000):
    if is_self_number(guess_number) == True:
        # 결과 출력
        print (guess_number)
