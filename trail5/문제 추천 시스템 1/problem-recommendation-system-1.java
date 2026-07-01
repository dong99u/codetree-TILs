import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        TreeSet<int[]> treeSet = new TreeSet<>(
            Comparator.comparingInt((int[] arr) -> arr[0])
                    .thenComparingInt((int[] arr) -> arr[1])
        );

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            treeSet.add(new int[] {l, p});
        }

        int m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            switch (st.nextToken()) {
                case "rc": {
                    int x = Integer.parseInt(st.nextToken());
                    int[] poll;
                    if (x == 1) {
                        poll = treeSet.last();
                    } else {
                        poll = treeSet.first();
                    }
                    sb.append(poll[1]).append("\n"); // 문제 번호 넣기.
                    break;
                }

                case "ad": {
                    int p = Integer.parseInt(st.nextToken());
                    int l = Integer.parseInt(st.nextToken());
                    treeSet.add(new int[] {l, p});
                    break;
                }

                case "sv": {
                    int p = Integer.parseInt(st.nextToken());
                    int l = Integer.parseInt(st.nextToken());
                    treeSet.remove(new int[] {l, p});
                    break;
                }
            }
        }
        System.out.println(sb);
    }
}