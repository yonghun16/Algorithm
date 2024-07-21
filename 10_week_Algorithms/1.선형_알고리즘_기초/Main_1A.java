// 문제1A 최대값 함수

import java.util.Scanner;

public class Main_1A {
    public static int getMax(int a, int b) {
        if (a > b) {
            return a;
        }
        else {
            return b;
        }
    }

    public static void main(String[] args) {
        int a, b;
        int answer;

        Scanner scanner = new Scanner(System.in);
        a = scanner.nextInt();
        b = scanner.nextInt();
        scanner.close();

        answer = getMax(a, b);
        System.out.println(answer);
    }
}
