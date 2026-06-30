import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        TreeSet<Integer> treeSet = IntStream.rangeClosed(1, m).boxed()
            .collect(Collectors.toCollection(TreeSet::new));

        st = new StringTokenizer(br.readLine());

        int answer = 0;
        for (int i = 0; i < n; i++) {
            int ai = Integer.parseInt(st.nextToken());
            Integer floor = treeSet.floor(ai);

            if (floor != null) {
                treeSet.remove(floor);
                answer++;
            } else {
                break;
            }

        }

        System.out.println(answer);
    }
}
