import java.io.*;
import java.util.*;

// BFS, 최단 경로 문제

public class solution55_yeji {

    public static int bfs(int start, int target) {
        if (start == target) return 0;

        boolean[] visited = new boolean[100001];
        Queue<int[]> queue = new LinkedList<>(); // [숫자, 연산 횟수] 저장

        // 초기 상태를 큐에 추가
        queue.offer(new int[] {start, 0});
        visited[start] = true; // 시작 숫자는 방문 처리

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int num = current[0];
            int count = current[1];

            // 세 가지 연산을 각각 수행
            int[] nextNums = {num-1, num+1, num*2};

            for (int next : nextNums) {
                if (next == target) {
                    return count + 1;
                }

                // 범위 내에 있고 아직 방문하지 않은 숫자만 큐에 추가
                if (next >= 0 && next <= 100000 && !visited[next]) {
                    queue.offer(new int[] {next, count + 1});
                    visited[next] = true;
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) throws IOException {
        java.util.Scanner sc = new java.util.Scanner(System.in);

        int target = sc.nextInt();
        int start = sc.nextInt();

        System.out.println(bfs(start, target));
    }
}
