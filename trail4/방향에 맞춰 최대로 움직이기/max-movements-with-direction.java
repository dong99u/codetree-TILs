import java.io.BufferedReader;
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static final int DIR_NUM = 8;

    // 1-indexed
    static int[] dx = {0, -1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dy = {0, 0, 1, 1, 1, 0, -1, -1, -1};

    static int n;
    static int[][] graph; // 숫자값 존재
    static int[][] direction; // 방향값 존재

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n]; // 0-indexed
        direction = new int[n][n];

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
    static int backtrack(int x, int y) {
        int sx = x, sy = y; // 맨 처음 시작 위치
        int dir = direction[x][y];
        int result = 0;
        while (true) {
            int nx = x + dx[dir], ny = y + dy[dir];
            if (!inRange(nx, ny))
                break;
            if (graph[nx][ny] > graph[sx][sy]) {
                result = Math.max(result, 1 + backtrack(nx, ny));
            }
            x = nx;
            y = ny;
        }
        return result;
    }

    static boolean inRange(int x, int y) {
        return (0 <= x && x < n) && (0 <= y && y < n);
    }

}
