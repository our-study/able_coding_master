import java.io.*;
import java.util.*;

// Binary Search

public class solution57_yeji {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        long X = sc.nextLong();
        long Y = sc.nextLong();

        long average = (Y * 100) / X;

        if (average >= 99) {
            System.out.println(-1);
            return;
        }

        long L = 0;
        long R = 1000000000;
        long result = -1;

        while (L <= R) {
            long mid = (L + R) / 2;

            long newAverage = ((Y + mid) * 100) / (X + mid);

            if (newAverage > average) {
                result = mid;
                R = mid - 1;
            } else {
                L = mid + 1;
            }
        }

        System.out.println(result);
    }
}
