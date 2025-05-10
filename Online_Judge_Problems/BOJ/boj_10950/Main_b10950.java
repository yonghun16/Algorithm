// A+B -3
// https://www.acmicpc.net/problem/10950

import java.util.ArrayList;
import java.util.Scanner;

public class Main_b10950 {

    // 두 수를 더하는 함수
    public static int getSum(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        ArrayList<Integer> answers = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            answers.add(getSum(a, b));
        }

        for (int answer : answers) {
            System.out.println(answer);
        }

        scanner.close();
    }
}
