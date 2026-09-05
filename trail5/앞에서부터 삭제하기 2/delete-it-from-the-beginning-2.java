import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException { 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.offer(arr[n - 1]);
        int sum = arr[n - 1];
        double answer = 0.0;
        for (int i = n - 2; i >= 1; i--) {
            pq.offer(arr[i]);
            sum += arr[i];
            int minVal = pq.poll();
            sum -= minVal;
            answer = Math.max(answer, (double)sum / (n - i - 1));
            pq.offer(minVal);
            sum += minVal;
        }
        System.out.printf("%.2f", answer);


    }
}