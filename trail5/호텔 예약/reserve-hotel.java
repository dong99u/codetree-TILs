import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        ArrayList<int[]> points = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int x1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());

            points.add(new int[] {x1, +1});
            points.add(new int[] {x2, -1});
        }

        points.sort(Comparator.comparingInt((int[] e) -> e[0])
            .thenComparingInt(e -> -e[1]));

        int count = 0;
        int maxCount = 0;
        for (int i = 0; i < 2 * n; i++) {
            int[] p = points.get(i);
            if (p[1] == 1) {
                count++;
                maxCount = Math.max(maxCount, count);
            } else {
                count--;
            }
        }
        System.out.println(maxCount);
    }
}
