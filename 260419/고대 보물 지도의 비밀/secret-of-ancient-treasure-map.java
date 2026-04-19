import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static final int INF = (int)1e9;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		int[] arr = new int[n];

		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		// dp 초기화
		int[][] dp = new int[n][k + 1];
		for (int i = 0; i < n; i++) {
			Arrays.fill(dp[i], -INF);
		}
		if (arr[0] >= 0) {
			dp[0][1] = arr[0];
		} else {
			dp[0][0] = arr[0];
		}

		for (int i = 1; i < n; i++) {
			if (arr[i] >= 0) { // arr[i] 가 양수일 때,
				for (int j = 0; j < k + 1; j++) {
					if (dp[i - 1][j] == -INF) {
						dp[i][j] = Math.max(dp[i - 1][j], arr[i]);
					} else {
						dp[i][j] = Math.max(dp[i][j], dp[i - 1][j] + arr[i]);
					}
				}
			} else {
				for (int j = 1; j < k + 1; j++) {
					dp[i][j] = Math.max(arr[i], dp[i - 1][j - 1] + arr[i]);
				}
			}
		}

		int answer = -INF;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < k + 1; j++) {
				answer = Math.max(answer, dp[i][j]);
			}
		}

		System.out.println(answer);
	}
}
