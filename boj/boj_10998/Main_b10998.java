// AxB
// https://www.acmicpc.net/problem/10998

import java.util.Scanner;

public class Main_b10998 {
  public static void main(String[] args) {
    int a, b;
    int results;

    Scanner scanner = new Scanner(System.in);

    a = scanner.nextInt();
    b = scanner.nextInt();

    results = a * b;

    System.out.println(results);

    scanner.close();
  }
}