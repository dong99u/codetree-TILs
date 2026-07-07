import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> emptyComputerNumbers = IntStream.rangeClosed(1, n)
            .boxed()
            .collect(Collectors.toCollection(PriorityQueue::new));

        ArrayList<int[]> points = new ArrayList<>();
        for (int i = 1; i < n + 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int x1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());

            points.add(new int[] {x1, +1, i});
            points.add(new int[] {x2, -1, i});
        }

        points.sort(Comparator.comparingInt((int[] e) -> e[0]));

        int[] results = new int[n + 1];
        for (int i = 0; i < 2 * n; i++) {
            int[] p = points.get(i);
            if (p[1] == 1) {
                results[p[2]] = emptyComputerNumbers.poll();
            } else
                emptyComputerNumbers.offer(results[p[2]]);
        }

        for (int i = 1; i < n + 1; i++) {
            System.out.print(results[i] + " ");
        }
    }
}
