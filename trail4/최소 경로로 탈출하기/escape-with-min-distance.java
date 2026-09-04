import java.util.*;
import java.io.*;

public class Main {
    static final int DIR_NUM = 4;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    static int n;
    static int m;
    static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = bfs();
        System.out.println(answer);

    }

    static int bfs() {
        int[][] dist = new int[n][m];
        for (int i = 0; i < n; i++) { // 거리 정보 초기화
            Arrays.fill(dist[i], -1);
        }
        ArrayDeque<int[]> queue = new ArrayDeque<>(Arrays.asList(new int[] {0, 0}));
        dist[0][0] = 0;
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int x = curr[0], y = curr[1];
            if (x == n - 1 && y == m - 1)
                return dist[n - 1][m - 1];

            for (int i = 0; i < DIR_NUM; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (!inRange(nx, ny))
                    continue;
                if (graph[nx][ny] == 0)
                    continue;
                if (dist[nx][ny] != -1)
                    continue;
                dist[nx][ny] = dist[x][y] + 1;
                queue.add(new int[] {nx, ny});
            }
        }
        return -1; // 도착 못하는 경우
    }

    static boolean inRange(int x, int y) {
        return (0 <= x && x < n) && (0 <= y && y < m);
    }
}
