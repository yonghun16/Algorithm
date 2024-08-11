import java.math.BigInteger;
import java.util.Scanner;

public class Main_b27433 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int N = scanner.nextInt();
        
        System.out.println(factorial(N));
    }

    public static BigInteger factorial(int n) {
        BigInteger result = BigInteger.ONE;
        
        for (int i = 2; i <= n; i++) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        
        return result;
    }
}
