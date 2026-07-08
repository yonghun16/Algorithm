# ⚙️ 위치 계산 보조 함수
def get_coords(x, w_val):
    # 상자 번호 x가 몇 번째 층(row), 몇 번째 열(col)에 있는지 구하는 함수 (0-index 기반)
    row = (x - 1) // w_val
    remainder = (x - 1) % w_val

    if row % 2 == 0:
        col = remainder  # 짝수 층: 왼쪽 -> 오른쪽
    else:
        col = w_val - 1 - remainder  # 홀수 층: 오른쪽 -> 왼쪽

    return row, col


# ⚙️ Core Logic
def solution(n, w, num):
    row, col = get_coords(num, w)
    last_row, last_col = get_coords(n, w)

    # 1. 꼭대기 바로 전 층까지 확실하게 존재하는 상자의 개수
    answer = last_row - row

    # 2. 맨 꼭대기 층(last_row)의 같은 열(col)에 상자가 있는지 확인
    if last_row % 2 == 0:
        top_box_num = last_row * w + col + 1
    else:
        top_box_num = last_row * w + (w - 1 - col) + 1

    # 꼭대기 방에 있는 상자 번호가 전체 상자 개수 n 이하라면 실재하는 상자임
    if top_box_num <= n:
        answer += 1

    return answer
