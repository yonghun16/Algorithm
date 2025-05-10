// 별 찍기 - 1
// https://www.acmicpc.net/problem/2438

import java.util.Scanner;

public class Main_b2439 {

    // 별을 출력하는 함수
    public static void printStar(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();

        printStar(n);
    }
}
