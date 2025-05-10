// N 찍기
// https://www.acmicpc.net/problem/2741

import java.util.Scanner;

public class Main_b2741 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        for (int i = 1; i <= n; i++) {
            System.out.println(i);
        }

        scanner.close();
    }
}
