import java.util.*;
import java.io.*;

public class Main {
    static final int MAX_VALUE = (int)1e6 + 1;

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

        int j = -1;
        int count = 0;
        int answer = MAX_VALUE;
        for (int i = 0; i < n; i++) {
            while (j + 1 < n && count < k) {
                if (arr[j + 1] == 1)
                    count++;
                j++;
            }
            if (count >= k)
                answer = Math.min(answer, j - i + 1);
            if (arr[i] == 1)
                count--;
        }
        System.out.println(answer != MAX_VALUE ? answer : -1);
    }
}
