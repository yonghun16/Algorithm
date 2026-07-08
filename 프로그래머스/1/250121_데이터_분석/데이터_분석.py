"""
-----------------------------------------------------------
Sub    : [Programmers] 데이터 분석
Link   : https://school.programmers.co.kr/learn/courses/30/lessons/250121
Level  : 1
Tag    : Python,
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""


def solution(data, ext, val_ext, sort_by):
    # 1. 항목별 인덱스 위치를 딕셔너리로 정의합니다.
    index_dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    # 2. 필터링 기준(ext)과 정렬 기준(sort_by)의 인덱스를 찾습니다.
    ext_idx = index_dict[ext]
    sort_idx = index_dict[sort_by]

    # 3. 리스트 컴프리헨션을 사용하여 ext 값이 val_ext보다 작은 데이터만 뽑습니다.
    filtered_data = [d for d in data if d[ext_idx] < val_ext]

    # 4. 정렬 기준 인덱스(sort_idx)를 기준으로 오름차순 정렬합니다.
    # key=lambda x: x[sort_idx]를 사용하면 해당 인덱스 값을 기준으로 정렬됩니다.
    filtered_data.sort(key=lambda x: x[sort_idx])

    return filtered_data
