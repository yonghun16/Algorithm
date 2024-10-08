// 검증수
// https://www.acmicpc.net/problem/2475

import java.util.Scanner;

public class Main_b2475 {

    // 검증수를 구하는 함수
    public static int getVerification(int[] numbers) {
        int sum = 0;
        for (int i = 0; i < 5; i++) {
            sum += numbers[i] * numbers[i];
        }
        return sum % 10;
    }

    public static void main(String[] args) {
        int[] numbers = new int[5];
        int answer;

        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 5; i++) {
            numbers[i] = scanner.nextInt();
        }
        scanner.close();

        answer = getVerification(numbers);
        System.out.println(answer);
    }
}
