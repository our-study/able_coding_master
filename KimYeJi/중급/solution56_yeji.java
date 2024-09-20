import java.io.*;
import java.util.*;

// 최장 증가 부분 수열(LIS), Dynamic Programming
// 점화식 : dp[i] = max(dp[i], dp[j] + 1)

public class solution56_yeji {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] sharks = new int[N];

        for (int i = 0; i < N; i++) {
            sharks[i] = sc.nextInt();
        }

        int[] dp = new int[N];
        for (int i = 0; i < N; i++) {
            dp[i] = 1;
        }

        // LIS 알고리즘
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < i; j++) {
                if (sharks[j] < sharks[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int result = 0;
        for (int i = 0; i < N; i++) {
            result = Math.max(result, dp[i]);
        }

        System.out.println(result);
    }
}
