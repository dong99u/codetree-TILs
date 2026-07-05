import java.util.*;
import java.io.*;

public class Main {
    static final int INF = (int)1e9;
    static final int K = 3;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[n + 2][K + 1];

        for (int i = 0; i < K; i++) {
            dp[n][i] = -INF;
            dp[n + 1][i] = -INF;
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j < K; j++) {
                dp[i][j] = Math.max(arr[i] + dp[i + 2][j + 1], dp[i + 1][j]);
            }
        }

        System.out.println(dp[0][0]);
    }
}
