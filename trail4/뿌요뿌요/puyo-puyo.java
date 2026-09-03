import java.util.*;
import java.io.*;

public class Main {
    static final int DIR_NUM = 4;
    static int[] dxs = {1, 0, -1, 0};
    static int[] dys = {0, 1, 0, -1};

    static int n;
    static int[][] graph;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        visited = new boolean[n][n];

        int boomCount = 0;
        int maxCount = 0;
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                if (!visited[x][y]) {
                    visited[x][y] = true;
                    int result = dfs(x, y);
                    if (result >= 4) { // 블럭이 4개 이상이라면 터져야한다.
                        boomCount++;
                    }
                    if (maxCount < result) {
                        maxCount = result;
                    }
                }
            }
        }
        System.out.println(boomCount + " " + maxCount);
    }

    static int dfs(int x, int y) {
        int result = 1;
        for (int i = 0; i < DIR_NUM; i++) {
            int nx = x + dxs[i], ny = y + dys[i];
            if (!inRange(nx, ny))  // 범위 밖이면
                continue;
            if (graph[x][y] != graph[nx][ny])
                continue;
            if (visited[nx][ny])
                continue;
            visited[nx][ny] = true;
            result += dfs(nx, ny);
        }
        return result;
    }

    static boolean inRange(int x, int y) {
        return (0 <= x && x < n) && (0 <= y && y < n);
    }
}
