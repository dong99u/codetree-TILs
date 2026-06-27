import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        HashMap<String, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            char[] c = br.readLine().toCharArray();
            Arrays.sort(c);
            String s = String.valueOf(c);
            hashMap.merge(s, 1, Integer::sum);
        }

        int answer = hashMap.entrySet().stream().max(Comparator.comparingInt(e -> e.getValue()))
            .get().getValue();

        System.out.println(answer);
    }
}
