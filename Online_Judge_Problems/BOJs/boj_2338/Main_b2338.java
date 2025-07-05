// 긴자리 계산
// https://www.acmicpc.net/problem/2338

import java.math.BigInteger;
import java.util.Scanner;

public class Main_b2337 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the two large numbers from input
        String strA = scanner.nextLine().trim();
        String strB = scanner.nextLine().trim();

        // Parse the numbers as BigInteger
        BigInteger A = new BigInteger(strA);
        BigInteger B = new BigInteger(strB);

        BigInteger sum = A.add(B);
        BigInteger difference = A.subtract(B);
        BigInteger product = A.multiply(B);

        // Print the results
        System.out.println(sum.toString());
        System.out.println(difference.toString());
        System.out.println(product.toString());
        
        scanner.close();
    }
}
