//! 입력 패턴 모음 (Rust 2021).
//! 각 패턴은 `&str`을 받아 값을 돌려주는 순수 함수로 작성했고, `cargo test`로 검증할 수 있습니다.
//! 실제 제출 시에는 필요한 함수만 복사해서 `main`에서 사용하세요.
#![allow(dead_code)]

use std::fmt::Debug;
use std::io::{self, Read};
use std::str::FromStr;

// ───────────── 공통 헬퍼 ─────────────

/// stdin 전체를 한 번에 읽는다 (대부분의 문제에서 가장 빠르고 단순).
fn read_input() -> String {
    let mut buf = String::new();
    io::stdin()
        .read_to_string(&mut buf)
        .expect("stdin 읽기 실패");
    buf
}

/// "3 5" -> vec![3, 5]  (T는 반환 타입으로 추론)
fn parse_vec<T>(line: &str) -> Vec<T>
where
    T: FromStr,
    T::Err: Debug,
{
    line.split_whitespace()
        .map(|x| x.parse().expect("숫자 파싱 실패"))
        .collect()
}

// ───────────── 1. 숫자 하나 ─────────────
// 3
fn parse_one<T>(input: &str) -> T
where
    T: FromStr,
    T::Err: Debug,
{
    input.trim().parse().expect("파싱 실패")
}

// ───────────── 2. 한 줄 → 각각의 숫자 변수 ─────────────
// 3 5
fn parse_pair(input: &str) -> (i32, i32) {
    let mut it = input
        .split_whitespace()
        .map(|x| x.parse::<i32>().expect("숫자 파싱 실패"));
    (it.next().expect("입력 부족"), it.next().expect("입력 부족"))
}

// ───────────── 3. 한 줄 → 벡터 ─────────────
// 1 2 3 4 5 6 7 8 9
fn parse_numbers(input: &str) -> Vec<i32> {
    parse_vec(input)
}

// ───────────── 4. 한 줄 → 각각의 문자열 변수 ─────────────
// abc def
fn parse_two_words(input: &str) -> (&str, &str) {
    let mut it = input.split_whitespace();
    (it.next().expect("입력 부족"), it.next().expect("입력 부족"))
}

// ───────────── 5. 문자열 n줄 → 1차원 벡터 ─────────────
// ABCDEF
// BCDEFA
// CDEFAB
fn parse_lines(input: &str, n: usize) -> Vec<&str> {
    input.lines().take(n).map(str::trim).collect()
}

// ───────────── 6. 공백 없는 숫자 n줄 → 2차원 벡터 ─────────────
// 0101
// 1010
// 2020
fn parse_digit_grid(input: &str, n: usize) -> Vec<Vec<u8>> {
    input
        .lines()
        .take(n)
        .map(|line| line.trim().bytes().map(|b| b - b'0').collect())
        .collect()
}

// 문자 격자: 공백 없는 문자 n줄 → Vec<Vec<char>>
fn parse_char_grid(input: &str, n: usize) -> Vec<Vec<char>> {
    input
        .lines()
        .take(n)
        .map(|line| line.trim().chars().collect())
        .collect()
}

// ───────────── 7. 공백 구분 숫자 n줄 → 2차원 벡터 ─────────────
// 0 1 0 1
// 1 0 1 0
// 2 0 2 0
fn parse_int_grid(input: &str, n: usize) -> Vec<Vec<i32>> {
    input.lines().take(n).map(parse_vec).collect()
}

// ───────────── 8. 첫 줄 T, 이후 T줄에 숫자 하나씩 ─────────────
// 3
// 1
// 2
// 3
fn parse_counted_numbers(input: &str) -> Vec<i32> {
    let mut lines = input.lines();
    let t: usize = parse_one(lines.next().expect("입력 부족"));
    lines.take(t).map(parse_one).collect()
}

// ───────────── 9. 첫 줄 "n m", 이어서 n줄 격자 ─────────────
fn parse_board(input: &str) -> (usize, usize, Vec<Vec<i32>>) {
    let mut lines = input.lines();
    let header: Vec<usize> = parse_vec(lines.next().expect("입력 부족"));
    let (n, m) = (header[0], header[1]);
    let board = lines.take(n).map(parse_vec).collect();
    (n, m, board)
}

// ───────────── 10. 줄 수를 모를 때 (끝까지, 가변 길이) ─────────────
fn parse_ragged(input: &str) -> Vec<Vec<&str>> {
    input
        .lines()
        .filter(|line| !line.trim().is_empty())
        .map(|line| line.split_whitespace().collect())
        .collect()
}

// ───────────── 11. 토큰 스캐너 (줄 구조가 불규칙하거나 입력이 클 때) ─────────────
struct Scanner<'a> {
    tokens: std::str::SplitAsciiWhitespace<'a>,
}

impl<'a> Scanner<'a> {
    fn new(input: &'a str) -> Self {
        Self {
            tokens: input.split_ascii_whitespace(),
        }
    }

    /// 다음 토큰 하나를 T로 파싱
    fn read<T>(&mut self) -> T
    where
        T: FromStr,
        T::Err: Debug,
    {
        self.tokens
            .next()
            .expect("입력 부족")
            .parse()
            .expect("파싱 실패")
    }

    /// 다음 n개 토큰을 Vec<T>로
    fn vec<T>(&mut self, n: usize) -> Vec<T>
    where
        T: FromStr,
        T::Err: Debug,
    {
        (0..n).map(|_| self.read()).collect()
    }
}

// ───────────── 12. 입력 파일을 직접 읽기 (로컬 테스트용) ─────────────
fn read_file_numbers(path: &str) -> io::Result<Vec<i32>> {
    let text = std::fs::read_to_string(path)?;
    Ok(parse_counted_numbers(&text))
}

// ───────────── 사용 예 ─────────────
fn solve(arr: &[i64]) -> i64 {
    arr.iter().sum()
}

fn main() {
    let input = read_input();
    let mut sc = Scanner::new(&input);
    let n: usize = sc.read();
    let arr: Vec<i64> = sc.vec(n);
    println!("{}", solve(&arr));
}

// ───────────── 테스트: cargo test ─────────────
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_and_pair() {
        assert_eq!(parse_one::<i32>("3\n"), 3);
        assert_eq!(parse_pair("3 5\n"), (3, 5));
    }

    #[test]
    fn vectors_and_words() {
        assert_eq!(parse_numbers("1 2 3"), vec![1, 2, 3]);
        assert_eq!(parse_two_words("abc def"), ("abc", "def"));
    }

    #[test]
    fn line_patterns() {
        assert_eq!(
            parse_lines("ABCDEF\nBCDEFA\nCDEFAB\n", 3),
            vec!["ABCDEF", "BCDEFA", "CDEFAB"]
        );
        assert_eq!(
            parse_digit_grid("0101\n1010\n2020\n", 3),
            vec![vec![0, 1, 0, 1], vec![1, 0, 1, 0], vec![2, 0, 2, 0]]
        );
        assert_eq!(
            parse_int_grid("0 1\n1 0\n", 2),
            vec![vec![0, 1], vec![1, 0]]
        );
    }

    #[test]
    fn counted_and_board() {
        assert_eq!(parse_counted_numbers("3\n1\n2\n3\n"), vec![1, 2, 3]);
        assert_eq!(
            parse_board("2 3\n1 2 3\n4 5 6\n"),
            (2, 3, vec![vec![1, 2, 3], vec![4, 5, 6]])
        );
    }

    #[test]
    fn ragged_and_scanner() {
        assert_eq!(
            parse_ragged("A -1 B -1\n\nA -1 C -1\n"),
            vec![vec!["A", "-1", "B", "-1"], vec!["A", "-1", "C", "-1"]]
        );
        let mut sc = Scanner::new("3\n10 20 30\n");
        let n: usize = sc.read();
        assert_eq!(sc.vec::<i64>(n), vec![10, 20, 30]);
    }
}

