// AxB -7
// https://www.acmicpc.net/problem/11021

import java.util.Scanner;
import java.util.ArrayList;

public class Main {
  public static void Main_b110221(String[] args) {
    Scanner scanner = new Scanner(System.in);
    ArrayList<Integer> results = new ArrayList<>();

    int t = scanner.nextInt();

    for (int i = 0; i < t; i++) {
      int a = scanner.nextInt();
      int b = scanner.nextInt();

      results.add(a+b);
    }

    for (int i = 0; i < t; i++) {
      System.out.printf("Case #%d: %d\n", i+1, results.get(i));
    }

    scanner.close();
  }
}