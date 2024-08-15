// 윤년

import java.util.Scanner;

public class Main_b2753 {
    public static void main(String[] args) {
        // Scanner 객체를 사용하여 사용자로부터 연도를 입력받습니다.
        Scanner scanner = new Scanner(System.in);
        int year = scanner.nextInt();

        // 윤년인지 확인하는 조건
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            System.out.println(1);  // 윤년이면 1 출력
        } else {
            System.out.println(0);  // 윤년이 아니면 0 출력
        }

        // Scanner 객체를 닫습니다.
        scanner.close();
    }
}

