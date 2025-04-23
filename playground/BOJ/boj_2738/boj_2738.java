import java.util.Scanner;

public class boj_2738 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 행렬의 크기 N과 M 입력받기
        int N = sc.nextInt();
        int M = sc.nextInt();

        // 두 개의 행렬 A와 B 선언
        int[][] A = new int[N][M];
        int[][] B = new int[N][M];

        // 첫 번째 행렬 A 입력받기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                A[i][j] = sc.nextInt();
            }
        }

        // 두 번째 행렬 B 입력받기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                B[i][j] = sc.nextInt();
            }
        }

        // 두 행렬의 합을 계산하여 출력
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(A[i][j] + B[i][j] + " ");
            }
            System.out.println(); // 행이 끝날 때마다 줄바꿈
        }

        sc.close();
    }
}
