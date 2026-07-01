import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        PriorityQueue<int[]> pq = new PriorityQueue<>(
            Comparator.comparingInt((int[] e) -> e[0] + e[1])
                    .thenComparingInt((int[] e) -> e[0])
                    .thenComparingInt((int[] e) -> e[1])
        );

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            pq.offer(new int[] {x, y});
        }

        for (int i = 0; i < m; i++) {
            int[] curPoint = pq.poll();
            curPoint[0] += 2;
            curPoint[1] += 2;
            pq.offer(curPoint);
        }

        int[] answer = pq.poll();
        System.out.println(answer[0] + " " + answer[1]);

    }
}