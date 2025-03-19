import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int T = sc.nextInt();
		int R = sc.nextInt();
		int C = sc.nextInt();
		String D = sc.next();

		// 상, 우, 좌, 하
		int[] dx = new int[] {-1, 0, 0, 1};
		int[] dy = new int[] {0, 1, -1, 0};

		int currX = R - 1;
		int currY = C - 1;

		int dirNum = getDir(D);

		for (int i = 0; i < T; i++) {
			int nextX = currX + dx[dirNum];
			int nextY = currY + dy[dirNum];

			if (!inRange(nextX, nextY, N)) {
				dirNum = 3 - dirNum;
				continue;
			}

			currX = nextX;
			currY = nextY;

		}

		int answerX = currX + 1;
		int answerY = currY + 1;

		System.out.println(answerX + " " + answerY);
	}

	private static int getDir(String dir) {
		int dirNum = 0;

		if (dir.equals("U")) {
			dirNum = 0;
		} else if (dir.equals("R")) {
			dirNum = 1;
		} else if (dir.equals("L")) {
			dirNum = 2;
		} else {
			dirNum = 3;
		}

		return dirNum;
	}
	private static boolean inRange(int x, int y, int n) {
		return 0 <= x && x < n && 0 <= y && y < n;
	}
}