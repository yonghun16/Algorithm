/*
----------------------------------------------
Sub : [BOJ] A+B-C
Link: https://www.acmicpc.net/problem/31403
Tag : JAVA, String
Memo
----------------------------------------------
*/

import java.util.Scanner;

public class boj_31403 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    // 입력 받기
    int A = scanner.nextInt();
    int B = scanner.nextInt();
    int C = scanner.nextInt();

    // 첫 번째 출력: A + B - C (수로 처리)
    int resultNumber = A + B - C;
    System.out.println(resultNumber);

    // 두 번째 출력: A, B를 문자열로 이어붙인 후 C를 뺀 결과
    String strA = Integer.toString(A);
    String strB = Integer.toString(B);
    String concat = strA + strB; // 문자열 이어붙이기

    // 이어붙인 문자열을 정수로 변환하고 C를 뺌
    int resultStringNumber = Integer.parseInt(concat) - C;
    System.out.println(resultStringNumber);

    scanner.close();
  }
}
