// A+B-2
// https://www.acmicpc.net/problem/2558

import java.util.Scanner;

public class Main_b2558 {

    // 두 수를 더하는 함수
    public static int getSum(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int a, b;
        int answer;

        Scanner scanner = new Scanner(System.in);
        a = scanner.nextInt();
        b = scanner.nextInt();
        scanner.close();

        answer = getSum(a, b);

        System.out.println(answer);

    }
}
