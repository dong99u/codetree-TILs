import java.util.*;
import java.io.*;

public class Main {
    static final int DIR_NUM = 4;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

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
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(bfs());

    }

    static int bfs() {
        ArrayDeque<int[]> queue = new ArrayDeque<>(Arrays.asList(new int[] {0, 0}));
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int x = curr[0], y = curr[1];
            if (x == n - 1 && y == m - 1)
                return 1;
            for (int i = 0; i < DIR_NUM; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (!inRange(nx, ny))
                    continue;
                if (graph[nx][ny] == 0) // 뱀이라면
                    continue;
                if (visited[nx][ny])
                    continue;
                queue.add(new int[] {nx, ny});
                visited[nx][ny] = true;
            }
        }
        return 0;
    }

    static boolean inRange(int x, int y) {
        return (0 <= x && x < n) && (0 <= y && y < m);
    }
}
