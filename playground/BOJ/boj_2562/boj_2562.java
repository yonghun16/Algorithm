import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int[] numbers = new int[9]; // 9개의 숫자를 저장할 배열
    int max = 0; // 최댓값을 저장할 변수
    int index = 0; // 최댓값이 몇 번째인지 저장할 변수

    // 숫자 입력받기
    for (int i = 0; i < 9; i++) {
      numbers[i] = sc.nextInt();
    }

    // 최댓값 찾기
    for (int i = 0; i < 9; i++) {
      if (numbers[i] > max) {
        max = numbers[i];
        index = i + 1; // 인덱스는 0부터 시작하므로, 몇 번째인지 출력하기 위해 +1
      }
    }

    // 결과 출력
    System.out.println(max);
    System.out.println(index);
  }
}
