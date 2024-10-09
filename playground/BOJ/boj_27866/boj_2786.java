/*
----------------------------------------------
Sub: [BOJ] 27866. 문자와 문자열
Link: https://www.acmicpc.net/problem/27866
Tag: Javascript, 문자열
Memo
- 문자열은 0부터 인덱스 시작
----------------------------------------------
*/

import java.util.Scanner;

public class boj_2786 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    // 문자열과 정수 입력 받기
    String S = sc.next();
    int i = sc.nextInt();

    // 문자 출력
    System.out.println(S.charAt(i - 1));

    sc.close();
  }
}
