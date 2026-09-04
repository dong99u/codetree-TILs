import java.util.*;
import java.io.*;

public class Main {
    static final int DIR_NUM = 4;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    static int n;
    static int k;
    static int[][] graph;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] startPoints = new int[k][2];
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 2; j++) {
                startPoints[i][j] = Integer.parseInt(st.nextToken()) - 1;
            }
        }
        int answer = bfs(startPoints);
        System.out.println(answer);

    }

    static int bfs(int[][] startPoints) {
        int count = 0;
        boolean[][] visited = new boolean[n][n];
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        for (int[] point : startPoints) {
            count++;
            int x = point[0], y = point[1];
            visited[x][y] = true;
            queue.add(point);
        }

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int x = curr[0], y = curr[1];
            for (int i = 0; i < DIR_NUM; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (!inRange(nx, ny))
                    continue;
                if (graph[nx][ny] == 1)
                    continue;
                if (visited[nx][ny])
                    continue;

                queue.offer(new int[] {nx, ny});
                visited[nx][ny] = true;
                count++;
            }
        }
        return count;
    }

    static boolean inRange(int x, int y) {
        return (0 <= x && x < n) && (0 <= y && y < n);
    }
}
