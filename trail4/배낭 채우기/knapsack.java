import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int m;
    static int[] weights;
    static int[] values;
    static int[][] memo;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        weights = new int[n];
        values = new int[n];
        memo = new int[n][m + 1];
        
        for (int i = 0; i < n; i++) {
            Arrays.fill(memo[i], -1);
        }

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            weights[i] = Integer.parseInt(st.nextToken());
            values[i] = Integer.parseInt(st.nextToken());
        }
        int answer = backtrack(0, 0);
        System.out.println(answer);

    }

    // label
    // currIdx: 고려해야할 보석의 인덱스
    // acc: 지금까지 선택한 보석의 누적 무게
    // 정의: currIdx 번째 보석을 고려할 때, acc 만큼 무게를 골랐을 때 앞으로 얻을 수 있는 최대 가치
    static int backtrack(int currIdx, int acc) {
        if (currIdx == n) {
            return 0;
        }
        if (memo[currIdx][acc] != -1) {
            return memo[currIdx][acc];
        }

        int result = 0;
        if (acc + weights[currIdx] <= m) {
            result = Math.max(result, 
                values[currIdx] + backtrack(currIdx + 1, acc + weights[currIdx]));
        }
        result = Math.max(result, backtrack(currIdx + 1, acc));

        memo[currIdx][acc] = result;

        return memo[currIdx][acc];
    }
}
