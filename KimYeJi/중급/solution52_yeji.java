import java.io.*;
import java.util.*;

// Dynamic Programming
// 점화식 : dp[i] = dp[i−1]*2 + dp[i−2]

public class solution52_yeji {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] dp = new int[N + 1];

        dp[1] = 3;
        if (N > 1) {
            dp[2] = 7;
        }

        for (int i = 3; i <= N; i++) {
            dp[i] = (dp[i - 1]*2 + dp[i - 2]) % 796796; // 오버플로우 방지를 위해 미리 모듈러 연산 수행
        }

        System.out.println(dp[N]);
    }
}
