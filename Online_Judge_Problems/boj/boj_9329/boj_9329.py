import sys


def solve():
    # 표준 입력으로부터 모든 데이터를 읽어와 단어 단위로 분리
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    # 첫 번째 값은 테스트 케이스의 개수
    num_test_cases = int(input_data[idx])
    idx += 1

    for _ in range(num_test_cases):
        # n: 상금 종류의 수, m: 스티커 종류의 수
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2

        prizes = []
        for _ in range(n):
            # k: 필요한 스티커 개수
            k = int(input_data[idx])
            # k개의 스티커 번호와 마지막 상금 액수를 추출
            prize_info = list(map(int, input_data[idx + 1 : idx + k + 2]))
            prizes.append(prize_info)
            idx += k + 1

        # 코치가 가진 1번부터 m번까지의 스티커 개수
        sticker_counts = list(map(int, input_data[idx : idx + m]))
        idx += m

        total_cash = 0

        for prize in prizes:
            # prize의 마지막 요소는 상금 액수, 그 앞까지는 필요한 스티커 번호들
            required_stickers = prize[:-1]
            cash_amount = prize[-1]

            # 이 상금을 만들기 위해 필요한 스티커들 중 최소 개수 찾기
            # 스티커 번호는 1부터 시작하므로 인덱스는 번호-1
            min_stickers = min(sticker_counts[s - 1] for s in required_stickers)

            # (해당 상금 액수 * 가능한 횟수)를 총합에 더함
            total_cash += min_stickers * cash_amount

        print(total_cash)


if __name__ == "__main__":
    solve()
