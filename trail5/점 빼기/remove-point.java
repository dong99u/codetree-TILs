import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        TreeSet<int[]> treeSet = new TreeSet<>(
            Comparator.comparingInt((int[] e) -> e[0])
                .thenComparingInt((int[] e) -> e[1])
        );

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            treeSet.add(new int[] {x, y});
        }

        for (int i = 0; i < m; i++) {
            int k = Integer.parseInt(br.readLine());
            int[] val = treeSet.ceiling(new int[] {k, Integer.MIN_VALUE});

            if (val != null) {
                sb.append(val[0]).append(" ").append(val[1]).append("\n");
                treeSet.remove(val);
            } else {
                sb.append("-1 -1\n");
            }


        }

        System.out.println(sb);
    }

}
