/* ------------------------------------------------------------
 * File     : ArrayListBasic.java
 * Brief    : ArrayList 연습용 기본 클래스
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------ */

import java.util.ArrayList;
import java.util.Scanner;

/** ArrayList 연습용 기본 클래스. */
public class ArrayListBasic {

  /** 두 수를 더하는 함수. */
  public static int getSum(int a, int b) {
    return a + b;
  }

  /** 프로그램 시작점. */
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    ArrayList<Integer> results = new ArrayList<>();

    // 입력이 더 이상 없을 때까지 반복해서 읽습니다.
    while (scanner.hasNextInt()) {
      int a = scanner.nextInt();
      int b = scanner.nextInt();

      results.add(getSum(a, b));
    }

    // 결과를 출력합니다.
    for (int result : results) {
      System.out.println(result);
    }

    scanner.close();
  }
}
