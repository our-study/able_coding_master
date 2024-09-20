import java.io.*;
import java.util.*;

// 그리디 알고리즘

public class solution54_yeji {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[][] convenience = new int[N][2];

        for (int i = 0; i < N; i++) {
            convenience[i][0] = sc.nextInt(); // 편의점 위치
            convenience[i][1] = sc.nextInt(); // 편의점에서 얻을 수 있는 포만감
        }

        int L = sc.nextInt();
        int P = sc.nextInt();

        // 편의점 위치 기준으로 오름차순 정렬
        Arrays.sort(convenience, (a, b) -> Integer.compare(a[0], b[0]));

        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        int visit = 0; // 편의점 방문 횟수
        int full = P; // 현재 포만감
        int idx = 0; // 현재 편의점 위치를 가리키는 인덱스

        while (full < L) {
            // 현재 포만감으로 방문할 수 있는 편의점을 모두 큐에 넣음
            while (idx < N && convenience[idx][0] <= full) {
                pq.offer(convenience[idx][1]);
                idx++;
            }

            if (pq.isEmpty()) {
                System.out.println(-1);
                return;
            }

            full += pq.poll();
            visit++;
        }

        System.out.println(visit);
    }
}
