import java.util.*;
import java.io.*;

public class Main {
    static int n; // 가로
    static int m; // 세로

    static int[][] graph;
    static boolean[][] visited;

    static int[] dxs = {1, 0};
    static int[] dys = {0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int answer = 0;
        dfs(0, 0);
        if (visited[n - 1][m - 1]) // 도착 했다면 1
            answer = 1;
        System.out.println(answer);

    }

    static void dfs(int cx, int cy) {
        for (int i = 0; i < 2; i++) {
            int dx = dxs[i], dy = dys[i];
            int nx = cx + dx, ny = cy + dy;
            if (canGo(nx, ny)) {
                visited[nx][ny] = true;
                dfs(nx, ny);
            }
        }
    }

    static boolean canGo(int x, int y) {
        if (!inRange(x, y))
            return false;
        if (graph[x][y] == 0)
            return false;
        if (visited[x][y])
            return false;
        return true;
    }

    static boolean inRange(int x, int y) {
        return (0 <= x && x < n) && (0 <= y && y < m);
    }
}
