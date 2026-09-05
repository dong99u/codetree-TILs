import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int[][] arr;
    static int[][] memo;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n][2];
        memo = new int[n][1001];
        for (int i = 0; i < n; i++) {
            Arrays.fill(memo[i], -1);
        }

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i] = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        }

        Arrays.sort(arr, Comparator.comparingInt((int[] e) -> e[1]).thenComparingInt(e -> e[0]));

        int answer = backtrack(0, 0);
        System.out.println(answer);
    }

    // label
    // curr: 현재 선택하고자 하는 선분의 인덱스 -> 인자 o
    // prev: 마지막으로 선택한 선분의 끝점
    static int backtrack(int currIdx, int prev) {
        if (currIdx == n) {
            return 0;
        }
        if (memo[currIdx][prev] != -1) {
            return memo[currIdx][prev];
        }
        int x1 = arr[currIdx][0];
        int x2 = arr[currIdx][1];
        int result = 0;
        if (x1 > prev) {
            result = Math.max(result, backtrack(currIdx + 1, x2) + 1);
        }
        result = Math.max(result, backtrack(currIdx + 1, prev));
        memo[currIdx][prev] = result;
        return memo[currIdx][prev];
    }
}
