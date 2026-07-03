import java.util.*;
import java.io.*;

public class Main {
    static final int MAX_RANGE = 1000000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());

        int[] arr = new int[MAX_RANGE + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(st.nextToken());
            arr[x] += 1;
        }

        int[] prefixSum = new int[MAX_RANGE + 1];
        for (int i = 1; i < MAX_RANGE + 1; i++) {
            prefixSum[i] = prefixSum[i - 1] + arr[i];
        }

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            sb.append(prefixSum[b] - prefixSum[a] + arr[a]).append("\n");
        }

        System.out.println(sb);
        
    }
}
