def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        # 1. 해당 직원의 출근 인정 마지노선 시간 계산
        sh = schedules[i] // 100
        sm = schedules[i] % 100
        
        # 10분을 더함
        sm += 10
        if sm >= 60:
            sh += 1
            sm -= 60
        
        limit_time = sh * 100 + sm
        
        # 2. 일주일 동안 지각했는지 여부 체크
        is_success = True
        
        for day_idx in range(7):
            # 현재 요일 계산 (startday가 1~7이므로 day_idx를 더하고 7로 나눈 나머지 활용)
            # 결과가 6 또는 0(일요일)이면 주말이므로 체크 안 함
            current_day = (startday + day_idx - 1) % 7 + 1
            
            # 토요일(6)이나 일요일(7)은 패스
            if current_day == 6 or current_day == 7:
                continue
                
            # 평일인데 마지노선 시간을 넘겨서 출근했다면 지각!
            if timelogs[i][day_idx] > limit_time:
                is_success = False
                break  # 한 번이라도 지각하면 이 직원은 탈락이므로 중단
                
        # 일주일 동안 한 번도 지각 안 했다면 상품 수령자 추가
        if is_success:
            answer += 1
            
    return answer