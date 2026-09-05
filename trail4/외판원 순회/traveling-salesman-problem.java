import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int[][] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n + 1][n + 1];
        visited = new boolean[n + 1];
        visited[1] = true;

        for (int i = 1; i < n + 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j < n + 1; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = backtrack(0, 1);
        System.out.println(answer);
    }

    static int backtrack(int depth, int curr) {
        // 마지막 노드에 도착하면 거기서 다시 노드 1 로 돌아가야한다.
        if (depth == n - 1) {
            if (graph[curr][1] != 0)
                return graph[curr][1];
            else
                return (int)1e9;
        }
        int result = (int)1e9;
        for (int next = 1; next < n + 1; next++) {
            if (!visited[next] && graph[curr][next] != 0) {
                visited[next] = true;
                result = Math.min(result, graph[curr][next] + backtrack(depth + 1, next));
                visited[next] = false;
            }
        }
        return result;
    }
}
