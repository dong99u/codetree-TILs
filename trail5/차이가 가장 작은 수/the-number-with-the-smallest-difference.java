import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        TreeSet<Integer> treeSet = new TreeSet<>();

        for (int i = 0; i < n; i++) {
            treeSet.add(Integer.parseInt(br.readLine()));
        }

        int answer = Integer.MAX_VALUE;
        for (Integer i : treeSet) {
            Integer cur = treeSet.ceiling(i + m);
            if (cur != null) {
                answer = Math.min(answer, cur - i);

            }

        }
        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);

    }
}
