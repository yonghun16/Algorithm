import sys


def solve():
    # 입력 속도를 높이기 위해 sys.stdin.read를 사용합니다.
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    # 첫 번째 값은 N (티켓의 수)
    n = int(input_data[0])
    # 두 번째 값부터는 티켓 번호 리스트 (중복 제거 후 정렬)
    tickets = sorted(list(set(map(int, input_data[1:]))))

    # 우리가 찾고 있는 가장 작은 번호 (1번부터 시작)
    smallest_available = 1

    for ticket in tickets:
        # 현재 티켓 번호가 우리가 찾는 번호와 같다면
        # 그다음 번호를 확인하기 위해 1을 증가시킵니다.
        if ticket == smallest_available:
            smallest_available += 1
        # 만약 현재 티켓 번호가 우리가 찾는 번호보다 크다면
        # 그 사이 번호가 비어있다는 뜻이므로 반복을 종료합니다.
        elif ticket > smallest_available:
            break

    print(smallest_available)


if __name__ == "__main__":
    solve()
