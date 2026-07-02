import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] A = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int[] B = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(A);
        Arrays.sort(B);

        PriorityQueue<int[]> pq = new PriorityQueue<>(
            Comparator.comparingInt((int[] arr) -> arr[0])
                    .thenComparingInt(arr -> arr[1])
                    .thenComparingInt(arr -> arr[2])
        );

        for (int i = 0; i < n; i++) {
            pq.offer(new int[] {A[i] + B[0], i, 0});
        }

        int count = 0;
        int answer = 0;
        while (!pq.isEmpty()) {
            int[] arr = pq.poll();
            count++;
            if (count == k) {
                answer = arr[0];
                break;
            }
            if (arr[2] + 1 < m) pq.offer(new int[] {A[arr[1]] + B[arr[2] + 1], arr[1], arr[2] + 1});
        }

        System.out.println(answer);

    }
}