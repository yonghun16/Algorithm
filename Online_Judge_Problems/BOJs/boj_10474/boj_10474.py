'''
----------------------------------------------
Sub : [BOJ] 분수좋아해?
Link: https://www.acmicpc.net/problem/10474
Tag : Python, 
Memo
----------------------------------------------
'''

while True:
    line = input().strip()
    if line == "0 0":
        break
    
    numerator, denominator = map(int, line.split())
    
    # 대분수 변환
    integer_part = numerator // denominator
    remainder = numerator % denominator
    
    if remainder == 0:
        print(f"{integer_part} 0 / {denominator}")
    else:
        print(f"{integer_part} {remainder} / {denominator}")
