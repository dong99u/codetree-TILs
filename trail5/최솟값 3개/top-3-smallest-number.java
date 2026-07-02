import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            pq.offer(num);

            if (pq.size() < 3) {
                sb.append(-1).append("\n");
            } else {
                long[] arr = new long[3];
                for (int j = 0; j < 3; j++) {
                    arr[j] = pq.poll();
                }
                long result = Arrays.stream(arr).reduce((a, b) -> a * b).getAsLong();
                sb.append(result).append("\n");

                for (int j = 0; j < 3; j++) {
                    pq.offer((int)arr[j]);
                }
            }
        }
        System.out.println(sb);
    }
}