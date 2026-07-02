import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>(
            Comparator.reverseOrder()
        );

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            pq.offer(Integer.parseInt(st.nextToken()));
        }

        while (pq.size() >= 2) {
            int a = pq.poll();
            int b = pq.poll();

            if (a - b != 0)
                pq.offer(Math.abs(a - b)); 
        }
        Integer answer = pq.poll();
        System.out.println(answer == null ? -1 : answer);
    }
}