import math

# ⚙️ Core Logic
def solution(signals):
    if not signals:
        return -1

    cycles = [g + y + r for g, y, r in signals]

    # 모든 신호등 주기의 최소공배수(LCM) 계산
    max_time = 1
    for c in cycles:
        max_time = math.lcm(max_time, c)

    # 0초부터 (최소공배수 - 1)초까지 시뮬레이션
    for t_prime in range(max_time):
        all_yellow = True

        for g, y, r in signals:
            cycle = g + y + r
            mod_t = t_prime % cycle

            # 노란불 구간인지 확인 (G <= 나머지 < G + Y)
            if not (g <= mod_t < g + y):
                all_yellow = False
                break

        if all_yellow:
            ans = t_prime + 1  # 문제는 1초부터 시작하므로 1을 더해줌
            print(ans)
            return ans

    # 최소공배수 주기 내에 모두 노란불이 되는 경우가 없다면 영원히 없음
    print(-1)
    return -1

