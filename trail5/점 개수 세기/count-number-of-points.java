import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        TreeSet<Integer> xSet = new TreeSet<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            xSet.add(Integer.parseInt(st.nextToken()));
        }

        HashMap<Integer, Integer> mapper = new HashMap<>();
        int cnt = 1;
        for (Integer num : xSet) {
            mapper.put(num, cnt++);
        }

        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken()), x2 = Integer.parseInt(st.nextToken());

            Integer start = xSet.ceiling(x1);
            Integer end = xSet.floor(x2);

            if (start == null || end == null) {
                sb.append(0).append("\n");
                continue;
            }

            int startIdx = mapper.get(start);
            int endIdx = mapper.get(end);

            if (startIdx > endIdx) {
                sb.append(0).append("\n");
                continue;
            }
            sb.append(mapper.get(end) - mapper.get(start) + 1).append("\n");
        }
        System.out.println(sb);
    }
}
