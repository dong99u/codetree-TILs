import java.util.*;
import java.io.*;

public class Main {
    static final int MAX_X = 1_000_000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = new int[MAX_X + 1];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int count = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());

            arr[x] += count;
        }

        int sum = 0;
        for (int i = 0; i < Math.min(MAX_X, 2 * k); i++) {
            sum += arr[i];
        }

        int answer = sum;
        int j = 2 * k;
        for (int i = 0; i < MAX_X - Math.min(2 * k, MAX_X); i++) {
            sum += arr[++j];
            sum -= arr[i];
            answer = Math.max(answer, sum);
        }
        System.out.println(answer);
    }
}
