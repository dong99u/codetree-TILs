import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        TreeSet<Integer> removed = new TreeSet<>();
        TreeMap<Integer, Integer> segment = new TreeMap<>(
            Comparator.reverseOrder()
        );
        segment.put(n + 1, 1);

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int val = Integer.parseInt(st.nextToken());
            removed.add(val); // TreeSet에 넣기
            Integer lo = removed.lower(val);
            Integer hi = removed.higher(val);

            int leftLength = lo == null ? val : val - lo - 1;
            int rightLength = hi == null ? n - val : hi - val - 1;

            int target = leftLength + rightLength + 1;

            segment.merge(target, -1, Integer::sum);
            if (segment.get(target) == 0) segment.remove(target);
            segment.merge(leftLength, 1, Integer::sum);
            segment.merge(rightLength, 1, Integer::sum);

            sb.append(segment.firstEntry().getKey()).append("\n");
        }
        System.out.println(sb);
    }
}