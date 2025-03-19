import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] arr = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				arr[i][j] = sc.nextInt();
			}
		}

		int[] dx = new int[] {0, 1, 0, -1}; // 오른쪽, 아래, 왼쪽, 위 순서
		int[] dy = new int[] {1, 0, -1, 0};

		int answer = 0;

		for (int x = 0; x < n; x++) {
			for (int y = 0; y < n; y++) {

				int count = 0;
				for (int i = 0; i < 4; i++) {
					int nx = x + dx[i];
					int ny = y + dy[i];

					if (!inRange(nx, ny, n)) {
						continue;
					}

					if (arr[nx][ny] == 1) {
						count++;
					}
				}

				if (count >= 3) {
					answer++;
				}
			}
		}

		System.out.println(answer);
	}

	private static boolean inRange(int x, int y, int n) {
		return 0 <= x && x < n && 0 <= y && y < n;
	}
}