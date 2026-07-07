import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        ArrayList<int[]> points = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken());
            int x1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());

            points.add(new int[] {x1, +1, y, i});
            points.add(new int[] {x2, -1, y, i});
        }

        points.sort(Comparator.comparingInt((int[] e) -> e[0]));

        PriorityQueue<int[]> pq = new PriorityQueue<>(
            Comparator.comparingInt((int[] e) -> e[0])
        );
        HashSet<Integer> results = new HashSet<>();
        HashMap<Integer, Integer> deletedQueue = new HashMap<>();
        for (int i = 0; i < 2 * n; i++) {
            int[] p = points.get(i);
            if (p[1] == 1) {
                pq.offer(new int[] {p[2], p[3]});
                results.add(pq.peek()[1]);
            } else {
                if (pq.peek()[1] == p[3]) {
                    pq.poll();
                    while (!pq.isEmpty() && deletedQueue.getOrDefault(pq.peek()[1], 0) > 0) {
                        int id = pq.poll()[1];
                        deletedQueue.merge(id, -1, Integer::sum);
                    }
                } else {
                    deletedQueue.merge(p[3], 1, Integer::sum);
                }
                if (!pq.isEmpty())
                    results.add(pq.peek()[1]);
            }
        }

        System.out.println(results.size());
    }
}
