import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		PriorityQueue<Point> priorityQueue = new PriorityQueue<>(
			Comparator.comparingInt((Point p) -> p.x + p.y)
				.thenComparingInt(a -> a.x)
				.thenComparingInt(a -> a.y)
		);

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());

			priorityQueue.add(new Point(x, y));
		}

		for (int i = 0; i < m; i++) {
			Point p = priorityQueue.poll();
            p.updatePoint();
            priorityQueue.add(p);
		}

		Point answer = priorityQueue.poll();

		System.out.println(answer.x + " " + answer.y);
	}

	private static class Point {
		int x;
		int y;

		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}

		public void updatePoint() {
			this.x += 2;
			this.y += 2;
		}

	}
}
