// 두 수 비교하기
// https://www.acmicpc.net/problem/1330

import java.util.Scanner;

public class b1330 {
    
    // 두 정수를 비교하고 결과 출력
    public static String compare(int a, int b) {
        if (a > b) {
            return ">";
        } else if (a < b) {
            return "<";
        } else {
            return "==";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();

        scanner.close();

        System.out.println(compare(a, b));
    }
}
