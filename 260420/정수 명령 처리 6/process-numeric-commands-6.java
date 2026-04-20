import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String order = st.nextToken();

			switch (order) {
				case "push":
					priorityQueue.add(Integer.parseInt(st.nextToken()));
					break;

				case "pop":
					System.out.println(priorityQueue.poll());
					break;

				case "size":
					System.out.println(priorityQueue.size());
					break;

				case "empty":
					System.out.println(priorityQueue.isEmpty() ? 1 : 0);
					break;

				case "top":
					System.out.println(priorityQueue.peek());
					break;


			}
		}
	}
}
