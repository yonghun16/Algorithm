// A+B - 6
// https://www.acmicpc.net/problem/10953

import java.util.Scanner;
import java.util.ArrayList;

public class Main_b10953 {

    // 두 수를 더하는 함수
    public static int getSum(int a, int b) {
        return a + b;
    }

    public static void main(String[] args){
        int a, b;
        int n;
        ArrayList<Integer> results = new ArrayList<>();

        Scanner scanner = new Scanner(System.in);

        n = scanner.nextInt();
        scanner.nextLine();  // 개행 문자를 읽어서 제거합니다.

        for (int i = 0; i < n; i++) {
            String line = scanner.nextLine();
            String[] numbers = line.split(",");
            a = Integer.parseInt(numbers[0].trim());
            b = Integer.parseInt(numbers[1].trim());

            results.add(getSum(a, b));
        }

        for (int result : results) {
            System.out.println(result);
        }

        scanner.close();
    }
}
