import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());		

		PriorityQueue<Integer> pq = new PriorityQueue<>(
			Comparator.reverseOrder()
		);

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			int val = Integer.parseInt(st.nextToken());
			pq.offer(val);
		}

		for (int i = 0; i < m; i++) {
			int val = pq.poll();
			val--;
			pq.offer(val);
		}

		System.out.println(pq.poll());
    }
}