/* -----------------------------------------------------------
 * Sub    : [JOL] 연필 공장
 * Link   : https://jungol.co.kr/problem/5545
 * Level  : Silver 5
 * Tag    : Rust, Math
 * ------------------------------------------------------------
 * Approach
 * 도색은 (P+1)번째마다, 광택은 (V+1)번째마다 실패한다.
 * 둘 다 실패는 lcm(P+1, V+1)번째마다. 나눗셈으로 O(1) 계산.
 * ------------------------------------------------------------
 */
#![allow(unused)]

use std::io::{self, BufWriter, Read, Write};

fn read_input() -> String {
    std::fs::read_to_string("./input_test.txt").unwrap_or_else(|_| {
        let mut s = String::new();
        io::stdin().read_to_string(&mut s).unwrap();
        s
    })
}

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 { a } else { gcd(b, a % b) }
}

fn main() {
    let input = read_input();
    let mut it = input.split_ascii_whitespace();
    let mut out = BufWriter::new(io::stdout().lock());

    /* 📥 Input */
    let p: i64 = it.next().unwrap().parse().unwrap();
    let v: i64 = it.next().unwrap().parse().unwrap();
    let k: i64 = it.next().unwrap().parse().unwrap();

    /* ⚙️ Logic */
    let cp = p + 1; // 도색 주기
    let cv = v + 1; // 광택 주기
    let lcm = cp / gcd(cp, cv) * cv;

    let pf = k / cp; // 도색 실패
    let vf = k / cv; // 광택 실패
    let both = k / lcm; // 둘 다 실패

    let a = k - pf - vf + both;
    let b = both;
    let c = vf - both;
    let d = pf - both;

    /* 🚀 Output */
    writeln!(out, "{} {} {} {}", a, b, c, d).unwrap();
}
