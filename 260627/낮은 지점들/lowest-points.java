import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            if (hashMap.containsKey(x)) {
                if (hashMap.get(x) > y) {
                    hashMap.put(x, y);
                }
            } else {
                hashMap.put(x, y);
            }
        }

        long sum = hashMap.values()
            .stream()
            .mapToLong(e -> e)
            .sum();

        System.out.println(sum);
    }
}
