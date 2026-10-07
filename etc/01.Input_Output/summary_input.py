"""파이썬 입력 패턴 모음 (Python 3.9+). 필요한 함수만 복사해서 사용."""

import sys
from collections.abc import Callable
from itertools import islice
from typing import TypeVar

input = sys.stdin.readline

T = TypeVar("T")


# --- 한 줄 입력 ---
def read_int() -> int:
    """3 -> 3"""
    return int(input())


def read_ints() -> list[int]:
    """'3 5' -> [3, 5]  (언패킹: a, b = read_ints())"""
    return list(map(int, input().split()))


def read_words() -> list[str]:
    """'abc def' -> ['abc', 'def']"""
    return input().split()


def read_chars() -> list[str]:
    """'ABC' -> ['A', 'B', 'C']"""
    return list(input().strip())


# --- 여러 줄 입력 (줄 수를 아는 경우) ---
def read_lines(n: int) -> list[str]:
    """n줄 문자열 -> 1차원 리스트"""
    return [input().strip() for _ in range(n)]


def read_digit_grid(n: int) -> list[list[int]]:
    """공백 없는 숫자 n줄 ('0101') -> 2차원 int 리스트"""
    return [list(map(int, input().strip())) for _ in range(n)]


def read_char_grid(n: int) -> list[list[str]]:
    """공백 없는 문자 n줄 -> 2차원 문자 리스트"""
    return [list(input().strip()) for _ in range(n)]


def read_int_grid(n: int) -> list[list[int]]:
    """공백으로 구분된 숫자 n줄 -> 2차원 int 리스트"""
    return [read_ints() for _ in range(n)]


def read_rows(n: int, cast: Callable[[str], T]) -> list[list[T]]:
    """공백 구분 n줄 -> cast(int, float, str ...) 적용한 2차원 리스트"""
    return [[cast(x) for x in input().split()] for _ in range(n)]


# --- 줄 수를 모르는 경우 ---
def read_token_rows() -> list[list[str]]:
    """EOF까지 전부 읽어 줄별 토큰 리스트로 (가변 길이 가능)"""
    return [line.split() for line in sys.stdin if line.strip()]


def read_all_tokens() -> list[str]:
    """입력이 아주 클 때: 전부 읽어 공백 기준 토큰으로 분리"""
    return sys.stdin.read().split()


# --- 파일 입력 ---
def read_file_numbers(path: str) -> list[int]:
    """첫 줄 T, 이후 T줄에 숫자 하나씩"""
    with open(path, encoding="utf-8") as f:
        t = int(next(f))
        return list(map(int, islice(f, t)))


# --- 사용 예 ---
def solve(n: int, arr: list[int]) -> int:
    return sum(arr[:n])


def main() -> None:
    n = read_int()
    arr = read_ints()
    print(solve(n, arr))


if __name__ == "__main__":
    main()
