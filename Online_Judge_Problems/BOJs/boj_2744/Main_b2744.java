// 대소문자 바꾸기
// https://www.acmicpc.net/problem/2744

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        StringBuilder output = new StringBuilder();

        for (char ch : input.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                output.append(Character.toLowerCase(ch));
            } else if (Character.isLowerCase(ch)) {
                output.append(Character.toUpperCase(ch));
            }
        }

        System.out.println(output.toString());
        scanner.close();
    }
}
