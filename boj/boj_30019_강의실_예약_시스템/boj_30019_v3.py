import sys
input = sys.stdin.readline

# 입력받기
n, m = map(int, input().split())

arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

# 예약 시스템 기록의 룸 번호를 키로 해서 start, end를 저장할 딕셔너리 초기화
book = {}  # 일반 딕셔너리를 사용

for el in arr:
    room_number = el[0]
    start = el[1]
    end = el[2]
    
    # 룸 넘버가 예약되어 있는 경우
    if room_number in book:
        prev_start, prev_end = book[room_number]  # 기존 예약 범위
        
        # 새 예약이 이전 예약 이후인 경우 (겹치지 않음)
        if start >= prev_end:
            book[room_number] = [prev_start, end]
            print('YES')
        
        # 새 예약이 이전 예약 이전인 경우 (겹치지 않음)
        elif end <= prev_start:
            book[room_number] = [start, prev_end]
            print('YES')
        
        # 새 예약이 기존 예약과 겹치는 경우
        else:
            print('NO')
    
    # 룸 넘버가 예약되지 않은 경우
    else:
        book[room_number] = [start, end]
        print('YES')
