import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        TreeSet<Integer> treeSet = new TreeSet<>(Comparator.reverseOrder());

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            treeSet.add(Integer.parseInt(st.nextToken()));
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < k; i++) {
            sb.append(treeSet.pollFirst()).append(" ");
        }

        System.out.println(sb);

    }
}
