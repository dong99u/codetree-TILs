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
        visited = new boolean[n][n];
        ArrayList<Integer> results = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // 모든 집합 순회
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    visited[i][j] = true;
                    results.add(dfs(i, j));
                }
            }
        }

        Collections.sort(results); // 정렬

        System.out.println(results.size());
        for (int i : results) {
            System.out.println(i);
        }
    }

    static int dfs(int x, int y) {
        int result = 1;
        for (int i = 0; i < DIR_NUM; i++) {
            int dx = dxs[i], dy = dys[i];
            int nx = x + dx, ny = y + dy;

            if (canGo(nx, ny)) {
                visited[nx][ny] = true;
                result += dfs(nx, ny);
            }
        }
        return result;
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
        return (0 <= x && x < n) && (0 <= y && y < n);
    }
}
