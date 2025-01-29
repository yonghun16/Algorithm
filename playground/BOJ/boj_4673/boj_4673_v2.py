'''---------------------------------------------
Sub  : [BOJ] 셀프 넘버
Link : https://www.acmicpc.net/problem/4673
Level: 실버 5
Tag  : Python, 부루트포스
Memo
 - 
---------------------------------------------'''

s1 = set(range(1, 10000))  # 1부터 9999까지의 숫자 집합
s2 = set()

# 생성자가 있는 숫자를 계산
for i in s1:
    num = i
    for digit in str(i):  # 숫자를 문자열로 변환하여 각 자릿수를 더함
        num += int(digit)
    s2.add(num)  # 생성된 숫자를 s2에 추가

# 셀프 넘버 계산
s = sorted(s1 - s2)  # 전체 숫자에서 생성자가 있는 숫자를 뺀 후 정렬

# 결과 출력
for i in s:
    print(i)
