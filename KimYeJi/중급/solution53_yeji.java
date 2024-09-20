import java.io.*;
import java.util.*;

// Dynamic Programming
// 점화식 : dp[i] = min(dp[i], dp[i - coin] + 1)

public class solution53_yeji {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] coins = new int[N];
        for (int i = 0; i < N; i++) {
            coins[i] = sc.nextInt();
        }

        int[] dp = new int[M + 1];  // dp[i] = i를 만들기 위한 최소 동전 개수
        Arrays.fill(dp, 10001);
        dp[0] = 0;

        for (int coin : coins) {
            for (int i = coin; i <= M; i++) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }

        if (dp[M] == 10001) {
            System.out.println(-1);
        } else {
            System.out.println(dp[M]);
        }
    }
}
