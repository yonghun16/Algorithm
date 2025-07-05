/* 합 */
/* https://www.acmicpc.net/problem/8393 */

import java.util.*;

public class b8393 {
    public static void main(String[] args) {
        java.util.Scanner inputData = new java.util.Scanner(System.in);

        int n = inputData.nextInt();
        int sum = 0;

        for(int i = 1; i <= n; i++) {
            sum += i;
        }

        System.out.println(sum);
    }
}
