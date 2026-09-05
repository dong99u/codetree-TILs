import java.util.*;
import java.io.*;

public class Main {
    static final int DIR_NUM = 4;

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    static int n;
    static int[][] graph;
    static int[][] memo;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        memo = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                answer = Math.max(answer, backtrack(i, j));
            }
        }
        System.out.println(answer);
    }

    //label: (x, y) 현재 좌표
    // (x, y)에서 나갈 수 있는 최대 이동 횟수
    static int backtrack(int x, int y) {
        if (memo[x][y] != 0) {
            return memo[x][y];
        }
        int result = 1;
        for (int i = 0; i < DIR_NUM; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (!inRange(nx, ny)) {
                continue;
            }
            if (graph[nx][ny] > graph[x][y]) {
                result = Math.max(result, backtrack(nx, ny) + 1);
            }
        }
        memo[x][y] = result;
        return memo[x][y];
    }

    static boolean inRange(int x, int y) {
        return (0 <= x && x < n) && (0 <= y && y < n);
    }
}
