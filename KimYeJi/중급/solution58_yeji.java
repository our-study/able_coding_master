import java.io.*;
import java.util.*;

// Dynamic Programming
// 점화식 : dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + coin[i][j]

public class solution58_yeji {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[][] coins = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= i; j++) {
                coins[i][j] = sc.nextInt();
            }
        }

        int[][] dp = new int[N][N];
        dp[0][0] = coins[0][0];

        for (int i = 1; i < N; i++) {
            for (int j = 0; j <= i; j++) {
                if (j == 0) {   // 맨 왼쪽 열
                    dp[i][j] = dp[i-1][j] + coins[i][j];
                } else if (j == i) {    // 맨 오른쪽 열
                    dp[i][j] = dp[i-1][j-1] + coins[i][j];
                } else {
                    dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + coins[i][j];
                }
            }
        }

        int max = 0;
        for (int j = 0; j < N; j++) {
            max = Math.max(max, dp[N-1][j]);
        }

        System.out.println(max);
    }
}