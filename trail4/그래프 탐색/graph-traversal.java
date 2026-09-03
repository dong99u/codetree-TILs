import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int m;

    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new ArrayList[n + 1];
        visited = new boolean[n + 1];

        // 그래프 초기화
        for (int i = 0; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph[u].add(v);
            graph[v].add(u);
        }

        int answer = dfs(1) - 1;
        System.out.println(answer);
    }

    static int dfs(int v) {
        visited[v] = true;

        int result = 1;
        for (Integer next : graph[v]) {
            if (!visited[next]) { // 방문하지 않았다면
                result += dfs(next);
            }
        }
        return result;
    }
}
