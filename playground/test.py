x, y = map(int, input().split())

if x > 0 and y > 0 :
    print("1")
elif x < 0 and y > 0 :
    print("2")
elif x < 1 and y < 0 :
    print("3")
else :
    print("4")
