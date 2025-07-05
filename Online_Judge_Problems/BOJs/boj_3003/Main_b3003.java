// 킹, 퀸, 룩, 비숍, 나이트, 폰
// https://www.acmicpc.net/problem/3003

import java.util.Scanner;

public class Main_b3003 {

    public static void main(String[] args) {
        // 올바른 체스 말의 개수를 배열로 저장
        int[] correctPieces = {1, 1, 2, 2, 2, 8};

        // 입력을 받기 위한 Scanner 객체 생성
        Scanner scanner = new Scanner(System.in);

        // 입력된 체스 말의 개수를 저장할 배열
        int[] piecesOfInput = new int[6];

        // 입력 받기
        for (int i = 0; i < 6; i++) {
            piecesOfInput[i] = scanner.nextInt();
        }

        // 결과를 저장할 배열
        int[] results = new int[6];

        // 결과 계산
        for (int i = 0; i < 6; i++) {
            results[i] = correctPieces[i] - piecesOfInput[i];
        }

        // 결과 출력
        for (int i = 0; i < 6; i++) {
            System.out.print(results[i] + " ");
        }
        System.out.println(); // 마지막에 개행 추가

        // Scanner 객체 닫기
        scanner.close();
    }
}
