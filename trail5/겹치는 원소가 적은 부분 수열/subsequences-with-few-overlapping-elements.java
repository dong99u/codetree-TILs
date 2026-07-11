import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        HashMap<Integer, Integer> hashMap = new HashMap<>();
        int answer = 0;
        int j = -1;
        for (int i = 0; i < n; i++) {
            while (j + 1 < n && hashMap.getOrDefault(arr[j + 1], 0) < k) {
                hashMap.merge(arr[j + 1], 1, Integer::sum);
                j++;
            }
            answer = Math.max(answer, j - i + 1);
            hashMap.merge(arr[i], -1, Integer::sum);
        }

        System.out.println(answer);
    }
}
