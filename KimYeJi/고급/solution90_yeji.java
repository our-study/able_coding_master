import java.io.*;
import java.util.*;

// 아이디어
// 나머지가 같아지려면 수들의 차이가 M의 배수여야 함
// 각 수들의 차이의 공약수를 구해야 함
// 최대 공약수 먼저 구한 후, 최대 공약수의 약수 구하기

public class solution90_yeji {

    // 최대 공약수(GCD)를 구하는 함수
    public static int gcd(int a, int b) {
        if (b == 0) return a;

        return gcd(b, a % b);
    }

    // 주어진 수의 약수를 구하는 함수
    public static List<Integer> findDivisors(int n) {
        List<Integer> divisors = new ArrayList<>();

        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                divisors.add(i);

                if (i != n / i) {
                    divisors.add(n / i);
                }
            }
        }
        Collections.sort(divisors);

        return divisors;
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] nums = new int[N];

        for (int i = 0; i < N; i++) {
            nums[i] = sc.nextInt();
        }

        // 수들 간의 차이를 구하고 그 차이들의 최대 공약수 구하기
        int g = Math.abs(nums[1] - nums[0]);
        for (int i = 2; i < N; i++) {
            g = gcd(g, Math.abs(nums[i] - nums[i-1]));
        }

        // 최대 공약수의 약수 구하기
        List<Integer> divisors = findDivisors(g);

        for (int i = 0; i < divisors.size(); i++) {
            int divisor = divisors.get(i);
            System.out.print(divisor + \" \");
        }
    }
}