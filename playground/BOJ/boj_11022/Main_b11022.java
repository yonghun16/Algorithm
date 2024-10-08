// A-B -8
// https://www.acmicpc.net/problem/11022

import java.util.Scanner;

public class Main_b11022 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt(); // 첫 번째 줄에 테스트 케이스의 개수를 입력받음

        for (int i = 1; i <= T; i++) {
            int A = scanner.nextInt(); // 각 테스트 케이스의 A를 입력받음
            int B = scanner.nextInt(); // 각 테스트 케이스의 B를 입력받음
            int C = A + B; // A와 B의 합을 계산

            System.out.printf("Case #%d: %d + %d = %d%n", i, A, B, C); // 요구된 형식으로 출력
        }

        scanner.close(); // 스캐너를 닫아 자원 해제
    }
}
