import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(
            Comparator.reverseOrder()
        );

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());

            if (num == 0) {
                Integer poll = pq.poll();
                if (poll == null) {
                    System.out.println(0);
                } else {
                    System.out.println(poll);
                }
            } else {
                pq.offer(num);
            }
        }
    }
}