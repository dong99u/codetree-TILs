import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        TreeMap<Integer, Integer> treeMap = new TreeMap<>();
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        for (int i = 0; i < n; i++) {
            treeMap.put(arr[i], i + 1);
        }

        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            Map.Entry<Integer, Integer> right = treeMap.floorEntry(b);
            Map.Entry<Integer, Integer> left = treeMap.floorEntry(a);

            int rightValue = right.getValue() == null ? 0 : right.getValue();
            int leftValue = left.getValue() == null ? 0 : left.getValue();

            int result;
            if (a == left.getKey()) {
                result = rightValue - leftValue + 1;
            } else {
                result = rightValue - leftValue;
            }
            sb.append(result).append("\n");
        }
        System.out.println(sb);

    }
}
