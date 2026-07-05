import java.util.*;
import java.io.*;

public class Main {
    static final int INF = (int)1e9;

    static int n;
    static final int K = 3;

    static int[] arr;
    static int[][] memo;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        memo = new int[n + 1][3];
        for (int i = 0; i < n + 1; i++) {
            Arrays.fill(memo[i], -1);
        }

        int answer = backtrack(0, 0);
        System.out.println(answer);
    }

    static int backtrack(int idx, int count) {
        if (count == K) return 0;          // 성공 기저
        if (idx >= n) return -INF;         // 경계/실패 기저 (== 아니라 >=, 메모보다 위)
        if (memo[idx][count] != -1) return memo[idx][count];

        int pick = arr[idx] + backtrack(idx + 2, count + 1);
        int skip = backtrack(idx + 1, count);
        memo[idx][count] = Math.max(pick, skip);
        return memo[idx][count];
    }

}
