import java.io.*;
import java.util.*;

public class Main {
    static final int DIR_NUM = 8;

    // 1-indexed
    static int[] dx = {0, -1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dy = {0, 0, 1, 1, 1, 0, -1, -1, -1};

    static int n;
    static int[][] graph; // 숫자값 존재
    static int[][] direction; // 방향값 존재
    static int[][] memo; // 메모이제이션

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n]; // 0-indexed
        direction = new int[n][n];
        memo = new int[n][n];

        for (int i = 0; i < n; i++) {
            Arrays.fill(memo[i], -1);
        }

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                direction[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        // 시작점 위치
        // 0-indexed
        int sx = Integer.parseInt(st.nextToken()) - 1, sy = Integer.parseInt(st.nextToken()) - 1;

        int answer = backtrack(sx, sy);
        System.out.println(answer);
    }

    /**
     * @param x 시작점 위치 x
     * @param y 시작점 위치 y
     * @return 최대 이동 횟수
     */
    // label: 현재 좌표
    static int backtrack(int x, int y) {      // x, y = 이 노드. 절대 안 변함
        if (memo[x][y] != -1)
            return memo[x][y];
        int dir = direction[x][y];
        int result = 0;
        int cx = x, cy = y;                    // 커서는 따로
        while (true) {
            int nx = cx + dx[dir], ny = cy + dy[dir];
            if (!inRange(nx, ny))
                break;
            if (graph[nx][ny] > graph[x][y]) {
                result = Math.max(result, 1 + backtrack(nx, ny));
            }
            cx = nx;
            cy = ny;
        }
        memo[x][y] = result;
        return result;
    }

    static boolean inRange(int x, int y) {
        return (0 <= x && x < n) && (0 <= y && y < n);
    }

}
