import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        TreeMap<String, Integer> treeMap = new TreeMap<>();
        int count = 0;
        for (int i = 0; i < n; i++) {
            treeMap.merge(br.readLine(), 1, Integer::sum);
            count++;
        }

        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Integer> e : treeMap.entrySet()) {
            sb.append(e.getKey())
                .append(" ")
                .append(String.format("%.4f", ((double)e.getValue() / count) * 100))
                .append("\n");
        }
        System.out.println(sb);
    }
}
