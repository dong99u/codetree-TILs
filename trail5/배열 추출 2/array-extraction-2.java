import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int n = sc.nextInt();

        PriorityQueue<Integer> pq = new PriorityQueue<>(
            Comparator.comparingInt((Integer e) -> Math.abs(e))
                    .thenComparingInt(e -> e)
        );

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            if (num == 0) {
                if (pq.isEmpty()) {
                    sb.append(0).append("\n");
                } else {
                    sb.append(pq.poll()).append("\n");
                }
            } else {
                pq.offer(num);
            }
        }

        System.out.println(sb);
    }
}