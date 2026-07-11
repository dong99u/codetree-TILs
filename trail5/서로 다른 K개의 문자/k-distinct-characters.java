import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        String s = st.nextToken();
        int n = s.length();
        int k = Integer.parseInt(st.nextToken());

        HashMap<Character, Integer> hashMap = new HashMap<>();

        int answer = 0;
        int j = -1;
        for (int i = 0; i < n; i++) {
            while (j + 1 < n && !(!hashMap.containsKey(s.charAt(j + 1)) && hashMap.size() >= k)) {
                hashMap.merge(s.charAt(j + 1), 1, Integer::sum);
                j++;
            }
            answer = Math.max(answer, j - i + 1);
            hashMap.merge(s.charAt(i), -1, Integer::sum);
            if (hashMap.get(s.charAt(i)) == 0)
                hashMap.remove(s.charAt(i));
        }
        System.out.println(answer);
    }

}
