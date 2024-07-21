// 1부터 n까지 수 출력하기
// https://www.biko.kr/problem/1408
//
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);

        int n;
        scanf("%d", &n);
        if (n>100) {
            printf("n이 100을 초과하였습니다.");
        }
        else {
            for (int i=0; i<n; i++) {
                printf("%d\n", i+1);
            }
        }
    }
}
