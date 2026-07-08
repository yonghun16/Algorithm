/*
----------------------------------------------
Sub : [BOJ] 문자열
Link: https://www.acmicpc.net/problem/9086
Tag : C, 문자열
Memo
----------------------------------------------
*/

import java.util.Scanner;

public class boj_9086 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt(); // 테스트 케이스 개수
    sc.nextLine(); // 개행 문자 소비

    for (int i = 0; i < T; i++) {
      String str = sc.nextLine(); // 문자열 입력
      char firstChar = str.charAt(0); // 첫 글자
      char lastChar = str.charAt(str.length() - 1); // 마지막 글자
      System.out.println("" + firstChar + lastChar); // 두 글자 출력
    }

    sc.close();
  }
}
