import java.util.*;
import java.io.*;

public class Main {
    static final int DIR_NUM = 4;

    static int[] dxs = {1, 0, -1, 0};
    static int[] dys = {0, 1, 0, -1};

    static int n;
    static int m;
    static int[][] graph;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][m];

        int maxK = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                maxK = Math.max(maxK, graph[i][j]);
            }
        }

        int answerK = 1;
        int answer = 0;

        for (int k = 1; k < maxK; k++) {
            int count = 0;
            visited = new boolean[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (graph[i][j] > k && !visited[i][j]) {
                        visited[i][j] = true;
                        dfs(i, j, k);
                        count++;
                    }
                }
            }
            if (answer < count) {
                answerK = k;
                answer = count;
            }
        }

        System.out.println(answerK + " " + answer);

    }

    static void dfs(int x, int y, int k) {
        for (int i = 0; i < DIR_NUM; i++) {
            int dx = dxs[i], dy = dys[i];
            int nx = x + dx, ny = y + dy;

            if (canGo(nx, ny, k)) {
                visited[nx][ny] = true;
                dfs(nx, ny, k);
            }
        }
    }

    static boolean canGo(int x, int y, int k) {
        if (!inRange(x, y))
            return false;
        if (graph[x][y] <= k)
            return false;
        if (visited[x][y])
            return false;
        return true;
    }

    static boolean inRange(int x, int y) {
        return (0 <= x && x < n) && (0 <= y && y < m);
    }
}
