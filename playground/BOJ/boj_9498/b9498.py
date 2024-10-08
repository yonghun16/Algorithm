# 시험 성적
# https://www.acmicpc.net/problem/9498

inputVal = int(input().strip())

if inputVal >= 90:
    print("A")
elif inputVal >= 80:
    print("B")
elif inputVal >= 70:
    print("C")
elif inputVal >= 60:
    print("D")
else:
    print("F")
