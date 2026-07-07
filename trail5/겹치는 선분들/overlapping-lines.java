import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int curX = 0;
        ArrayList<int[]> points = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int dist = Integer.parseInt(st.nextToken());
            String dir = st.nextToken();

            if ("R".equals(dir)) {
                points.add(new int[] {curX, +1});
                points.add(new int[] {curX + dist, -1});
                curX += dist;
            } else {
                points.add(new int[] {curX - dist, +1});
                points.add(new int[] {curX, -1});
                curX -= dist;
            }
        }

        points.sort(Comparator.comparingInt((int[] e) -> e[0])
            .thenComparingInt(e -> e[1]));

        int cnt = 0;
        long total = 0;
        for (int i = 0; i < 2 * n; i++) {
            int[] p = points.get(i);

            if (i > 0 && cnt >= k) {
                total += p[0] - points.get(i - 1)[0];
            }

            cnt += p[1];
        }

        System.out.println(total);
    }
}
