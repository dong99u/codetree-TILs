import java.util.*;
import java.io.*;

public class Main {
    static final int INF = (int)1e9;

    static int n;
    static int m;
    static int k;

    static ArrayList<int[]>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(br.readLine());
        graph = new ArrayList[n + 1];

        for (int i = 0; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(new int[] {v, w});
            graph[v].add(new int[] {u, w});
        }

        int[] dists = new int[n + 1];
        Arrays.fill(dists, INF);
        dists[k] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt((int[] e) -> e[0])); // (거리, 정점)
        pq.offer(new int[] {0, k});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int dist = curr[0];
            int u = curr[1];

            if (dist > dists[u]) {
                continue;
            }
            for (int[] next : graph[u]) {
                int v = next[0];
                int w = next[1];
                if (dist + w < dists[v]) {
                    dists[v] = dist + w;
                    pq.offer(new int[] {dist + w, v});
                }
            }
        }

        for (int i = 1; i < n + 1; i++) {
            if (dists[i] == INF) {
                sb.append(-1);
            } else {
                sb.append(dists[i]);
            }
            sb.append("\n");
        }

        System.out.println(sb);

    }
}
