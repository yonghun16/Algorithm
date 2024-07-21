// 문제1B-원소의 합 구하기

import java.util.Scanner;

public class Main_1B {

    // 입력된 정수 배열의 합을 계산하는 함수
    public static int getSum(int[] inputNumbers) {
        int sum = 0;
        for (int num : inputNumbers) {
            sum += num;
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 첫 번째 줄에서 데이터의 수 n을 읽습니다.
        int n = scanner.nextInt();

        int[] inputNumbers = new int[n];

        // 두 번째 줄에서 공백으로 구분된 n개의 정수를 읽어옵니다.
        for (int i = 0; i < n; i++) {
            inputNumbers[i] = scanner.nextInt();
        }

        scanner.close();

        // 합계를 계산합니다.
        int answer = getSum(inputNumbers);

        // 결과를 출력합니다.
        System.out.println(answer);

    }
}
