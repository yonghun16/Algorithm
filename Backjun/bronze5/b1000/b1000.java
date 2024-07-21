// A+B
// https://www.acmicpc.net/problem/1000

import java.util.*;

public class b1000 {
    public static int getSum(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int a, b;
        int answer;

        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        sc.close();

        answer = getSum(a, b);

        System.out.println(answer);
    }
}

