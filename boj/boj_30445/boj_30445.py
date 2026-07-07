import sys


def solve():
    # 딱 한 줄만 읽어오고 줄바꿈 문자(\n)만 제거합니다.
    # strip()을 사용하면 문장 앞뒤의 의도된 공백까지 지워질 수 있으므로 rstrip('\n')이 안전합니다.
    line = sys.stdin.readline().rstrip("\n")

    if not line:
        return

    # 행복한 글자와 우울한 글자 집합
    happy_chars = {"H", "A", "P", "Y"}
    sad_chars = {"S", "A", "D"}

    p_h = 0
    p_g = 0

    # 한 글자씩 확인하며 점수 산출
    for char in line:
        # A 같은 글자는 두 곳에 모두 점수를 더해줘야 하므로 if-if 구조 사용
        if char in happy_chars:
            p_h += 1
        if char in sad_chars:
            p_g += 1

    # 조건에 따른 결과 출력
    if p_h == 0 and p_g == 0:
        # P_H와 P_G가 모두 0이면 행복 지수는 0.5 (50.00%)
        print("50.00")
    else:
        # 백분율 계산
        h_index = (p_h / (p_h + p_g)) * 100

        # 부동 소수점 오차를 최소화하기 위해 0.0000000001 같은 작은 값을 더해준 뒤
        # 포맷팅을 하거나, 아래처럼 표준 포맷팅을 사용합니다.
        # ":.2f"는 기본적으로 반올림을 수행합니다.
        print("{:.2f}".format(h_index + 1e-9 if h_index % 1 != 0.5 else h_index))
        # 일반적으로는 아래 코드로도 통과됩니다.
        # print(f"{h_index:.2f}")


if __name__ == "__main__":
    solve()
